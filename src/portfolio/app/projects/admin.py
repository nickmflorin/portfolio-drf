from django.contrib import admin

from portfolio.app.skills.admin import SkillProjectInline

from .forms import ProjectForm
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name']
    search_fields = ['name']
    form = ProjectForm
    exclude = ['content_type', 'object_id']
    inlines = [
        SkillProjectInline
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Project, ProjectAdmin)
