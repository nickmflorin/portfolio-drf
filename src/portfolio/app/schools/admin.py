from django.contrib import admin

from .forms import SchoolForm
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['name']
    search_fields = ['name']
    form = SchoolForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(School, SchoolAdmin)
