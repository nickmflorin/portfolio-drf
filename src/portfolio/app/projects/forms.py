import os
from django import forms
from django.forms.models import BaseInlineFormSet
from django.conf import settings
from django.core.exceptions import ValidationError

from portfolio.app.common.forms import form_validation

from .models import Project


class ProjectFileFormSet(BaseInlineFormSet):

    @property
    def image_file_count(self):
        file_count = 0
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            data = form.cleaned_data
            if data.get('DELETE') is False:
                ext = os.path.splitext(data['file'].name)[1]
                if ext in settings.IMAGE_EXTENSIONS:
                    file_count += 1
        return file_count

    @form_validation
    def validate_files(self, errors):
        if not self.image_file_count and self.instance.showcase:
            raise ValidationError(
                "Must include at least 1 project file when showcasing a project.")

    def clean(self):
        super(ProjectFileFormSet, self).clean()
        self.validate_files()


class ProjectFileForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    def validate_caption(self, data):
        errors = {}
        file = data.get('file')
        caption = data.get('caption')
        if file:
            ext = os.path.splitext(file.name)[1]
            if ext.lower() in settings.IMAGE_EXTENSIONS and not caption:
                errors['caption'] = (
                    "Must provide caption when the file is an image file."
                )
            elif ext.lower() not in settings.IMAGE_EXTENSIONS and caption:
                errors['caption'] = (
                    "Captions are only allowed for image files."
                )
        if errors:
            raise ValidationError(errors)

    def clean(self):
        data = super(ProjectFileForm, self).clean()
        self.validate_caption(data)
        return data


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    @form_validation
    def validate_showcase_description(self, data, errors):
        showcase = data['showcase']
        showcase_description = data.get('showcase_description')
        if showcase and not showcase_description:
            errors['showcase_description'] = (
                'Required when the project is to be showcased.'
            )

    def clean(self):
        data = super(ProjectForm, self).clean()
        self.validate_showcase_description(data)
        return data
