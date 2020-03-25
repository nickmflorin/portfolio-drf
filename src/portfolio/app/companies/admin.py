from django.contrib import admin

from .forms import CompanyForm
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name']
    search_fields = ['name']
    form = CompanyForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Company, CompanyAdmin)
