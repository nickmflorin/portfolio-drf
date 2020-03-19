from django.contrib import admin

from portfolio.app.projects.forms import ProjectForm
from portfolio.app.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name']
    search_fields = ['name']
    form = ProjectForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Project, ProjectAdmin)