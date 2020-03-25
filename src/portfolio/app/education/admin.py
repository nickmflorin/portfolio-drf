from django.contrib import admin

from .forms import EducationForm
from .models import Education


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ['school', 'degree', 'major']
    search_fields = ['school', 'degree', 'major']
    form = EducationForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Education, EducationAdmin)
