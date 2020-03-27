from django.contrib import admin

from .models import Skill


class SkillProjectInline(admin.TabularInline):
    model = Skill.projects.through
    extra = 1


class SkillCourseInline(admin.TabularInline):
    model = Skill.courses.through
    extra = 1


class SkillEducationInline(admin.TabularInline):
    model = Skill.educations.through
    extra = 1


class SkillExperienceInline(admin.TabularInline):
    model = Skill.experiences.through
    extra = 1


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ['name']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Skill, SkillAdmin)
