from django import forms

from .models import Project


class ProjectFileForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 128}),
        required=True,
    )

    class Meta:
        model = Project
        fields = '__all__'
