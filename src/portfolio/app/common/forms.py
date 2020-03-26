from django import forms


class HorizonForm(forms.ModelForm):

    def clean(self):
        # TODO: Validate that the start date is before the end date.
        data = super().clean()
        ongoing = data.get("ongoing")

        errors = {}
        if ongoing is True:
            for field in ('end_month', 'end_year'):
                if data.get(field):
                    errors[field] = (
                        "Cannot provide `%s` when education is ongoing." % field
                    )
        elif ongoing is False:
            for field in ('end_month', 'end_year'):
                if not data.get(field):
                    errors[field] = (
                        "Must provide `%s` when not education is not ongoing."
                        % field
                    )
        if errors:
            raise forms.ValidationError(errors)
        return data
