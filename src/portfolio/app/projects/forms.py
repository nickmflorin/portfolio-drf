from django import forms

from .models import Project


class ProjectFileForm(forms.ModelForm):
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 128}),
        required=False,
    )
    long_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 128}),
        required=False,
    )
    long_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Project
        fields = '__all__'
