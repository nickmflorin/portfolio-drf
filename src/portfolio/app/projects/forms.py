from django import forms

from .models import Project


class ProjectInlineForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 80}),
        required=True,
    )

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForm(ProjectInlineForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=True,
    )
