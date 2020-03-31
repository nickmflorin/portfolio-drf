from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from portfolio.app.skills.admin import SkillProjectInline

from .forms import ProjectForm, ProjectFileForm, ProjectFileFormSet
from .models import Project, ProjectFile


class ProjectInline(GenericStackedInline):
    model = Project
    form = ProjectForm
    extra = 1


class ProjectFileInline(admin.StackedInline):
    model = ProjectFile
    form = ProjectFileForm
    formset = ProjectFileFormSet
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name']
    search_fields = ['name']
    form = ProjectForm
    exclude = ['content_type', 'object_id']
    inlines = [
        ProjectFileInline,
        SkillProjectInline
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        # We have to prevent adding projects outside of the inline forms from
        # the other models because adding a new project without a content_type
        # or object_id will fail, and we do not want to expose those fields in
        # the admin because it is ugly.
        return False

    def save_related(self, request, form, formsets, change):
        """
        Since a Project must either belong to an Education or an Experience,
        any skills gained throughout the course of a Project must also be
        consumed in the containing Education or Experience.
        """
        value = super(ProjectAdmin, self).save_related(request, form, formsets, change)
        instance = form.instance

        for skill in instance.skills.all():
            if skill not in instance.content_object.skills.all():
                instance.content_object.skills.add(skill)
                instance.content_object.save()
        return value


admin.site.register(Project, ProjectAdmin)
