from django import forms

from portfolio.app.common.forms import HorizonForm
from .models import Experience


class ExperienceForm(HorizonForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Experience
        fields = '__all__'
