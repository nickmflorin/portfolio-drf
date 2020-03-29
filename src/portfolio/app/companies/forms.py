from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Company
        fields = '__all__'
