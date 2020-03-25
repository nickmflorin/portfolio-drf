from django.contrib import admin

from .forms import CourseForm
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['name']
    search_fields = ['name']
    form = CourseForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Course, CourseAdmin)
