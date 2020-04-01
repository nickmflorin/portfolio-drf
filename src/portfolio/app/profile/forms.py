from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    intro = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 128}),
        required=True,
        help_text=(
            "Intro text to be displayed on the landing page."
        )
    )

    class Meta:
        model = Profile
        fields = '__all__'
