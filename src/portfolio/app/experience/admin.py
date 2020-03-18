from django.contrib import admin

from portfolio.app.experience.forms import ExperienceForm, CompanyForm
from portfolio.app.experience.models import Experience, Company


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name']
    search_fields = ['name']
    form = CompanyForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


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
admin.site.register(Company, CompanyAdmin)
