from django import forms

from portfolio.app.common.forms import HorizonForm
from .models import Education


class EducationForm(HorizonForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 40}),
        required=False,
    )

    class Meta:
        model = Education
        fields = '__all__'
