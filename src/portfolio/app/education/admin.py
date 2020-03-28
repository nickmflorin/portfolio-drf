from django.contrib import admin

from portfolio.app.courses.admin import CourseInline
from portfolio.app.projects.admin import ProjectInline
from portfolio.app.skills.admin import SkillEducationInline

from .forms import EducationForm
from .models import Education


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ['school', 'degree', 'major']
    search_fields = ['school', 'degree', 'major']
    form = EducationForm
    inlines = [
        ProjectInline,
        CourseInline,
        SkillEducationInline
    ]
    fieldsets = (
        (None, {
            'fields': (
                'school', 'degree', 'major', 'minor', 'concentration',
                'gpa',
            )
        }),
        ('Dates Attended', {
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

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Education, EducationAdmin)
