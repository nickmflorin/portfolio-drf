from django import forms

from .models import School


class SchoolForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 128}),
        required=False,
        help_text="Description of the school's expertise and reputation."
    )

    class Meta:
        model = School
        fields = '__all__'
