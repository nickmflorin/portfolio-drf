from django import forms

from .models import Education, School


class SchoolForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = School
        fields = '__all__'


class EducationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    class Meta:
        model = Education
        fields = '__all__'

    def clean(self):
        data = super().clean()
        end_date = data.get("end_date")
        ongoing = data.get("ongoing")

        errors = {}
        if ongoing is True and end_date:
            errors['end_date'] = (
                "Cannot provide `end_date` when flagging education as ongoing."
            )
        elif ongoing is False and not end_date:
            errors['end_date'] = (
                "Must provide `end_date` when not flagging education as "
                "ongoing."
            )
        if errors:
            raise forms.ValidationError(errors)
        return data
