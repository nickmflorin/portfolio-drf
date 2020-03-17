from django import forms

from .models import Education


class EducationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Education
        fields = '__all__'
