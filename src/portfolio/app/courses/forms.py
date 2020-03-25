from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Course
        fields = '__all__'
