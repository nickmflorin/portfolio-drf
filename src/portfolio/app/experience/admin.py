from django.contrib import admin

from portfolio.app.projects.admin import ProjectInline
from portfolio.app.skills.admin import SkillExperienceInline

from .forms import ExperienceForm
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ['title', 'company']
    search_fields = ['title', 'company']
    form = ExperienceForm
    fieldsets = (
        (None, {
            'fields': ('company', 'title')
        }),
        ('Dates of Employment', {
            'fields': (
                ('start_month', 'start_year'),
                ('end_month', 'end_year'),
                'current'
            )
        }),
        (None, {
            'fields': ('description', )
        }),
    )
    inlines = [
        ProjectInline,
        SkillExperienceInline,
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Experience, ExperienceAdmin)
