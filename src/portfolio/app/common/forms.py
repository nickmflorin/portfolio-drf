import datetime
from django import forms


class HorizonForm(forms.ModelForm):

    def validate_for_current(self, data):
        errors = {}
        current = data["current"]
        if current is True:
            for field in ('end_month', 'end_year'):
                if data.get(field):
                    errors[field] = (
                        "Cannot provide `%s` when education is current." % field
                    )
        elif current is False:
            for field in ('end_month', 'end_year'):
                if not data.get(field):
                    errors[field] = (
                        "Must provide `%s` when not education is not current."
                        % field
                    )
        if errors:
            raise forms.ValidationError(errors)

    def validate_for_range(self, data):
        # At this point, end_month and end_year are guaranteed to be present if
        # current is False.
        errors = {}
        if data['current'] is False and data.get('start_year') and data.get('end_year'):
            start_date = datetime.date(data['start_year'], data['start_month'], 1)
            end_date = datetime.date(data['end_year'], data['end_month'], 1)
            if start_date >= end_date:
                message = (
                    "The end year and month must coincide with a date that "
                    "is after that of the start year and month."
                )
                errors.update(end_month=message, end_year=message)
            if errors:
                raise forms.ValidationError(errors)

    def clean(self):
        data = super(HorizonForm, self).clean()
        self.validate_for_current(data)
        self.validate_for_range(data)
        return data
