from django.contrib import admin

from .models import Skill


class SkillProjectInline(admin.StackedInline):
    model = Skill.projects.through
    extra = 1
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


class SkillCourseInline(admin.StackedInline):
    model = Skill.courses.through
    extra = 1
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


class SkillEducationInline(admin.StackedInline):
    model = Skill.educations.through
    extra = 1
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


class SkillExperienceInline(admin.StackedInline):
    model = Skill.experiences.through
    extra = 1
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ['name']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def save_related(self, request, form, formsets, change):
        """
        If a Skill belongs to a course, it must also belong to the consuming
        Education.  Similarly, if a Skill belongs to a project, it must also
        belong to the consuming Education or Experience.
        """
        value = super(SkillAdmin, self).save_related(request, form, formsets, change)
        instance = form.instance

        for course in instance.courses.all():
            if instance not in course.education.skills.all():
                course.education.skills.add(instance)
                # TODO: Maybe only have to save course.education
                course.save()

        for project in instance.projects.all():
            if instance not in project.content_object.skills.all():
                project.content_object.skills.add(instance)
                # TODO: Maybe only have to save project.content_object
                project.save()

        return value


admin.site.register(Skill, SkillAdmin)
