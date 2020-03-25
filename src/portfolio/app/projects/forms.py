from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=True,
    )

    class Meta:
        model = Project
        fields = '__all__'
