from django.utils.translation import ugettext_lazy as _

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class PortfolioModelList(modules.ModelList):
    def __init__(self, *args, **kwargs):
        super(PortfolioModelList, self).__init__(*args,
            draggable=False,
            deletable=False,
            collapsible=False,
            **kwargs
        )


class PortfolioAppList(modules.AppList):
    def __init__(self, *args, **kwargs):
        super(PortfolioAppList, self).__init__(*args,
            draggable=False,
            deletable=False,
            collapsible=False,
            **kwargs
        )


class PortfolioDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children += [
            PortfolioModelList(
                _('Education'),
                models=['portfolio.app.courses.*', 'portfolio.app.education.*'],
            ),
            PortfolioModelList(
                _('Experience'),
                models=['portfolio.app.companies.*', 'portfolio.app.experience.*'],
            ),
            PortfolioModelList(
                _('Projects & Skills'),
                models=['portfolio.app.skills.*', 'portfolio.app.projects.*'],
            ),
            PortfolioAppList(
                _('Administration'),
                models=('django.contrib.*',),
            ),
            modules.RecentActions(
                _('Recent Actions'), 5,
                draggable=False,
                deletable=False,
                collapsible=False,
            ),
            modules.LinkList(
                _('Help'),
                draggable=False,
                deletable=False,
                collapsible=False,
                children=[
                    # TODO: Make a link for the front end shell.
                    [_('Visit API'), '/api/v1/education'],
                    [_('Change Password'), reverse('%s:password_change' % site_name)],
                    [_('Log Out'), reverse('%s:logout' % site_name)],
                ]
            )

        ]


class PortfolioAppIndexDashboard(AppIndexDashboard):
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
        return super(PortfolioAppIndexDashboard, self).init_with_context(context)
