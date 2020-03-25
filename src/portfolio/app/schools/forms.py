from django import forms

from .models import School


class SchoolForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = School
        fields = '__all__'
