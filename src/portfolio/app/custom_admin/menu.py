try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class PortfolioMenu(Menu):
    def __init__(self, **kwargs):
        super(PortfolioMenu, self).__init__(**kwargs)
        self.children += [
            items.MenuItem(_('Home'), reverse('admin:index')),
            items.ModelList(
                _('Education'),
                models=[
                    'portfolio.app.courses.*',
                    'portfolio.app.schools.*',
                    'portfolio.app.education.*'
                ],
            ),
            items.ModelList(
                _('Experience'),
                models=[
                    'portfolio.app.companies.*',
                    'portfolio.app.experience.*'
                ],
            ),
            items.ModelList(
                _('Projects & Skills'),
                models=[
                    'portfolio.app.skills.*',
                    'portfolio.app.projects.*'
                ],
            ),
            items.ModelList(
                _('Administration'),
                models=(
                    'django.contrib.*',
                    'portfolio.app.profile.*',
                    'portfolio.app.comments.*'
                ),
            ),
        ]

    def init_with_context(self, context):
        return super(PortfolioMenu, self).init_with_context(context)
