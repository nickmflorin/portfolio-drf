from django.contrib import admin

from .forms import ExperienceForm
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ['title', 'company', 'start_date', 'end_date']
    search_fields = ['title', 'company']
    form = ExperienceForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Experience, ExperienceAdmin)
