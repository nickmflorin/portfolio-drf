from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from portfolio.app.skills.admin import SkillProjectInline

from .forms import ProjectForm, ProjectInlineForm
from .models import Project


class ProjectInline(GenericStackedInline):
    model = Project
    form = ProjectInlineForm
    extra = 1


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
