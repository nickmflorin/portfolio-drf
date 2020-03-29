from django import forms

from portfolio.app.common.forms import HorizonForm
from .models import Education


class EducationForm(HorizonForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 128}),
        required=False,
    )

    class Meta:
        model = Education
        fields = '__all__'

    def validate_gpa(self, data):
        gpa = data["gpa"]
        if gpa is not None:
            if gpa < 0.0 or gpa > 4.0:
                self._errors['gpa'] = (
                    self.error_class(["Value must be between 0.00 and 4.00"])
                )

    def clean(self):
        data = super(EducationForm, self).clean()
        self.validate_gpa(data)
        return data
