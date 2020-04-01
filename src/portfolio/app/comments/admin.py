from django.contrib import admin

from .forms import CommentForm
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['name']
    search_fields = ['name']
    form = CommentForm

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        # TODO: Remove.  We don't want to be able to add comments from the admin
        # outside of testing.
        return True


admin.site.register(Comment, CommentAdmin)
