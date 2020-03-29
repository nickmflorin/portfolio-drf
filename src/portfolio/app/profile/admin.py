from django.contrib import admin

from .forms import ProfileForm
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    form = ProfileForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Profile, ProfileAdmin)
