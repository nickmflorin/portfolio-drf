from django import forms

from .models import Experience


class ExperienceForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Experience
        fields = '__all__'

    def clean(self):
        data = super().clean()
        end_date = data.get("end_date")
        current = data.get("current")

        errors = {}
        if current is True and end_date:
            errors['end_date'] = (
                "Cannot provide `end_date` when flagging experience as current."
            )
        elif current is False and not end_date:
            errors['end_date'] = (
                "Must provide `end_date` when not flagging experience as "
                "current."
            )
        if errors:
            raise forms.ValidationError(errors)
        return data
