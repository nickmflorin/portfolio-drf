import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def form_validation(func):
    def inner(instance, *args):
        errors = {}
        func(instance, *args, errors=errors)
        if errors:
            raise ValidationError(errors)
    return inner


class HorizonForm(forms.ModelForm):

    def validate_for_current(self, data):
        current = data["current"]
        if current is True:
            for field in ('end_month', 'end_year'):
                if data.get(field):
                    raise forms.ValidationError(
                        _('Cannot provide %(value)s when set to current.'),
                        params={'value': field}
                    )
        elif current is False:
            for field in ('end_month', 'end_year'):
                if not data.get(field):
                    raise forms.ValidationError(
                        _('Must provide %(value)s when not set to current.'),
                        params={'value': field},
                    )

    def validate_for_range(self, data):
        # At this point, end_month and end_year are guaranteed to be present if
        # current is False.
        if data['current'] is False and data.get('start_year') and data.get('end_year'):
            start_date = datetime.date(data['start_year'], data['start_month'], 1)
            end_date = datetime.date(data['end_year'], data['end_month'], 1)
            if start_date >= end_date:
                self._errors['end_month'] = self._errors['end_year'] = self.error_class([
                    "The end year and month must coincide with a date that "
                    "is after that of the start year and month."
                ])

    def clean(self):
        data = super(HorizonForm, self).clean()
        self.validate_for_current(data)
        self.validate_for_range(data)
        return data
