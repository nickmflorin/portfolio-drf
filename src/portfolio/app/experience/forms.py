from django import forms

from .models import Experience, Company


class CompanyForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Company
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Experience
        fields = '__all__'
