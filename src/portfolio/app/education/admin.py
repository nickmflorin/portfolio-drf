from django.contrib import admin
from portfolio.app.education.models import Education, School


class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['name']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ['start_date', 'end_date', 'degree', 'major']
    search_fields = ['start_date', 'degree', 'major']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Education, EducationAdmin)
admin.site.register(School, SchoolAdmin)
