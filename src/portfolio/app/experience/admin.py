from django.contrib import admin

from .forms import ExperienceForm
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ['title', 'company']
    search_fields = ['title', 'company']
    form = ExperienceForm
    filter_horizontal = ('projects',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Experience, ExperienceAdmin)
