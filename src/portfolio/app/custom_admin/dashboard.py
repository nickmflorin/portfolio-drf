from django.apps import apps
from django.contrib.admin import site as admin_site
from django.utils.translation import ugettext_lazy as _
import six
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


def get_model_admin(model, request, obj=None):
    if isinstance(model, six.string_types):
        try:
            model = apps.get_model(model)
        except LookupError:
            return

    model_admin = admin_site._registry.get(model)
    if model_admin and model_admin.has_change_permission(request, obj):
        return model_admin


class PortfolioGroup(modules.Group):
    collapsible = False


class ModelList(modules.ModelList):
    collapsible = False


class LinkList(modules.LinkList):
    collapsible = False


class ModelLinkList(ModelList):
    """
    Functions like a LinkList, except that the items of the ``children``
    kwarg can be (for convenience) one of four possible types:

        - dict: (same as :class:`grappelli.dashboard.modules.LinkList`)

            {"title": "Foo", "url": "/foo/"}

        - :class:`~ModelObjectLinks`: Evaluates a queryset and returns
          change_view links that the user has permission to edit

            ModelObjectLinks(SomeModel, filters=Q(active=True))

        - :class:`str`: Returns a changelist_view for the model corresponding
          to the string (in the form "%(app_label)s.%(model_name)s).

        - :class:`~ModelClassLink`: Returns a changelist_view for the given
          model. Use this class if you would like to override the link text
          (``title``) or if you would like to suppress the add buttons (by
          settings ``add`` to ``False``).
    """

    def __init__(self, *args, **kwargs):
        self.add = kwargs.pop('add', None)
        self.alphabetical = kwargs.pop('alphabetical', False)
        super(ModelLinkList, self).__init__(*args, **kwargs)

    def init_with_context(self, context):
        if self._initialized:
            return
        self._initialized = True
        request = context['request']
        new_children = []
        for link in self.children:
            if isinstance(link, six.string_types):
                link = ModelClassLink(link)
            if hasattr(link, 'get_children'):
                if self.add is not None:
                    link.add = self.add
                new_children += list(link.get_children(request))
            elif hasattr(link, 'keys') and hasattr(link, 'pop'):
                # Check that either url or admin_url are in the link dict
                if 'url' in link and 'admin_url' not in link:
                    link['admin_url'] = link.pop('url')
                if 'admin_url' not in link:
                    continue
                new_children.append(link)

        if self.alphabetical:
            new_children.sort(key=lambda l: l['title'])

        self.children = new_children


class ModelClassLink(object):

    def __init__(self, model=None, title=None, add=True):
        self.model = model
        self.title = title
        self.add = add

    def get_children(self, request):
        model_admin = get_model_admin(self.model, request)
        if not model_admin:
            return []

        opts = model_admin.model._meta
        info = (opts.app_label, opts.model_name)
        model_dict = {
            'title': self.title or opts.verbose_name_plural.title(),
            'admin_url': reverse('admin:%s_%s_changelist' % info),
        }
        if self.add and model_admin.has_add_permission(request):
            model_dict['add_url'] = reverse('admin:%s_%s_add' % info)
        return [model_dict]


class ModelObjectLinks(object):

    def __init__(self, model=None, filters=None, title=None):
        self.model = model
        self.filters = filters or {}
        if six.callable(title):
            self.title = title
        elif isinstance(title, six.string_types):
            self.title = lambda o: title
        else:
            self.title = lambda o: "%s" % o

    def get_children(self, request):
        model_admin = get_model_admin(self.model, request)
        if not model_admin:
            return []
        # Use the real resolved model class (self.model might have been a string)
        self.model = model_admin.model
        qset = self.model._default_manager.complex_filter(self.filters)
        children = []
        opts = self.model._meta
        info = (opts.app_label, opts.model_name)
        for obj in qset:
            # Check again whether permissions exist for this specific object
            if not model_admin.has_change_permission(request, obj):
                continue
            children.append({
                'title': self.title(obj),
                'admin_url': reverse('admin:%s_%s_change' % info, args=[obj.pk]),
            })
        return children


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for src.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children += [
            modules.ModelList(
                _('Education'),
                models=['portfolio.app.courses.*', 'portfolio.app.education.*']
            )
        ]
        self.children += [
            modules.ModelList(
                _('Experience'),
                models=['portfolio.app.companies.*', 'portfolio.app.experience.*']
            )
        ]
        self.children += [
            modules.ModelList(
                _('Projects & Skills'),
                models=['portfolio.app.skills.*', 'portfolio.app.projects.*']
            )
        ]
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        self.children.append(modules.RecentActions(_('Recent Actions'), 5))
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                # TODO: Make a link for the front end shell.
                [_('Visit API'), '/api/v1/education'],
                [_('Change Password'), reverse('%s:password_change' % site_name)],
                [_('Log Out'), reverse('%s:logout' % site_name)],
            ]
        ))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for src.
    """
    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
