from django import forms

from .models import Course


class CourseInlineForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 80}),
        required=False,
    )

    class Meta:
        model = Course
        fields = '__all__'


class CourseForm(CourseInlineForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=False,
    )
