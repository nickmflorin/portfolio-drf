from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    intro = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=True,
    )

    class Meta:
        model = Profile
        fields = '__all__'
