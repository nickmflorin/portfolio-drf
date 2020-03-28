from django.utils.translation import ugettext_lazy as _

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class PortfolioDashboard(Dashboard):
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


class PortfolioAppIndexDashboard(AppIndexDashboard):
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
        return super(PortfolioAppIndexDashboard, self).init_with_context(context)
