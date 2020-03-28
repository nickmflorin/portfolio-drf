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


admin.site.register(Course, CourseAdmin)
