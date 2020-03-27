from django import forms
from django.contrib import admin

from .models import Course


class CourseInlineForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 80}),
        required=True,
    )

    class Meta:
        model = Course
        fields = '__all__'


class CourseInline(admin.TabularInline):
    model = Course
    form = CourseInlineForm
    extra = 1


class CourseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Course
        fields = '__all__'
