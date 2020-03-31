import os
from django import forms
from django.core.exceptions import ValidationError

from .models import Project


IMAGE_EXTENSIONS = ('.png', '.jpeg', '.jpg', '.gif')


class ProjectFileForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=False,
        help_text="Description of the file limited to 1024 characters."
    )

    class Meta:
        model = Project
        fields = '__all__'

    def validate_caption(self, data):
        errors = {}
        file = data.get('file')
        caption = data.get('caption')
        if file:
            ext = os.path.splitext(file.name)[1]
            if ext.lower() in IMAGE_EXTENSIONS and not caption:
                errors['caption'] = (
                    "Must provide caption when the file is an image file."
                )
            elif ext.lower() not in IMAGE_EXTENSIONS and caption:
                errors['caption'] = (
                    "Captions are only allowed  for image files."
                )
        if errors:
            raise ValidationError(errors)

    def clean(self):
        data = super(ProjectFileForm, self).clean()
        self.validate_caption(data)
        return data


class ProjectForm(forms.ModelForm):
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 128}),
        required=True,
        help_text=(
            "Description of the project limited to 256 characters. "
        )
    )
    long_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=False,
        help_text=(
            "Description of the project limited to 1024 characters. "
            "Allowed/required if display alone is checked."
        )
    )

    class Meta:
        model = Project
        fields = '__all__'

    def validate_long_description(self, data):
        errors = {}
        display_alone = data['display_alone']
        long_description = data.get('long_description')
        if display_alone and not long_description:
            errors['long_description'] = (
                'Required when display alone is checked.'
            )
        elif not display_alone and long_description:
            errors['long_description'] = (
                'Only allowed when display alone is checked.'
            )
        if errors:
            raise ValidationError(errors)

    def clean(self):
        data = super(ProjectForm, self).clean()
        self.validate_long_description(data)
        return data
