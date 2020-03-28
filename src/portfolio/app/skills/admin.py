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


admin.site.register(Skill, SkillAdmin)
