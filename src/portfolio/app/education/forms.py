from django import forms

from .models import Education, School


class SchoolForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = School
        fields = '__all__'


class EducationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Education
        fields = '__all__'
