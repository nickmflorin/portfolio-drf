from django import forms
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Project


class ProjectInlineForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 80}),
        required=True,
    )

    class Meta:
        model = Project
        fields = '__all__'


class ProjectInline(GenericTabularInline):
    model = Project
    form = ProjectInlineForm
    extra = 1


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=True,
    )

    class Meta:
        model = Project
        fields = '__all__'
