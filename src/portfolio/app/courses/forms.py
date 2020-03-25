from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Course
        fields = '__all__'
