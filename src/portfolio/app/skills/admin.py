from django.contrib import admin
from portfolio.app.skills.models import Skill


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ['name']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.register(Skill, SkillAdmin)
