from django.contrib import admin

from portfolio.app.skills.admin import SkillCourseInline

from .forms import CourseForm, CourseInlineForm
from .models import Course


class CourseInline(admin.StackedInline):
    model = Course
    form = CourseInlineForm
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['name']
    search_fields = ['name']
    form = CourseForm
    inlines = [
        SkillCourseInline
    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def save_related(self, request, form, formsets, change):
        """
        Since a Course must belong to an Education, any skills gained throughout
        the course of a Project must also be consumed in the containing
        Education.
        """
        value = super(CourseAdmin, self).save_related(request, form, formsets, change)
        instance = form.instance

        for skill in instance.skills.all():
            if skill not in instance.education.skills.all():
                instance.education.skills.add(skill)
                instance.education.save()
        return value


admin.site.register(Course, CourseAdmin)
