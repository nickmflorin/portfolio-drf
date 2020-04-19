import os
import re

from django import forms
from django.forms.models import BaseInlineFormSet
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

from portfolio.app.education.models import Education
from portfolio.app.experience.models import Experience

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


class ProjectInlineForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description')


class ProjectForm(ProjectInlineForm):

    education_or_experience = forms.ChoiceField(required=False)
    resume_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 128}),
        required=False,
        help_text=(
            "If included, will be used instead of the description for the auto "
            "generated resume."
        )
    )

    class Meta:
        model = Project
        fields = ('name', 'description', 'resume_description', 'showcase',
            'showcase_description', 'education_or_experience', 'include_in_resume')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # Since the Experience or Education is referenced as a GenericForeignKey
        # on the Project model, we have no way of directly changing this value
        # without individual char fields for object_id and content_type (which
        # is ugly).  We instead initialize the ChoiceField with all of the
        # Experience and Education objects.
        available_objects = (
            list(Education.objects.all()) + list(Experience.objects.all()))
        object_choices = [(None, '-----')]
        for obj in available_objects:
            object_choices.append([self._choice_value_for_model(obj), str(obj)])

        self.fields['education_or_experience'].choices = object_choices
        if self.instance.content_object:
            self.fields['education_or_experience'].initial = self._choice_value_for_model(
                self.instance.content_object)

    def _choice_value_for_model(self, obj):
        content_type_id = ContentType.objects.get_for_model(obj.__class__).id
        return "type:%s-id:%s" % (content_type_id, obj.id)

    def _model_for_choice_value(self, value):
        content_type_id = int(value.split('-')[0].split(':')[1])
        object_id = int(value.split('-')[1].split(':')[1])
        content_type = ContentType.objects.get(id=content_type_id)
        return content_type.model_class().objects.get(pk=object_id)

    @form_validation
    def validate_showcase_description(self, data, errors):
        showcase = data['showcase']
        education_or_experience = data['education_or_experience']

        showcase_description = data.get('showcase_description')
        if showcase is True and not showcase_description:
            errors['showcase_description'] = (
                'Required when the project is to be showcased.'
            )
        elif showcase is False and not education_or_experience:
            errors['education_or_experience'] = (
                'Only allowed to be null if the project is being showcased.'
            )

    @form_validation
    def validate_description(self, data, errors):
        education_or_experience = data['education_or_experience']

        description = data.get('description')
        if education_or_experience != "" and not description:
            errors['description'] = (
                'Required when the project is tied to an education or experience.'
            )

    @form_validation
    def validate_for_resume(self, data, errors):
        education_or_experience = data['education_or_experience']
        include_in_resume = data['include_in_resume']
        if not education_or_experience and include_in_resume:
            errors['include_in_resume'] = (
                "Cannot include in resume if the project is not tied to an "
                "education or experience."
            )

    def clean(self):
        data = super(ProjectForm, self).clean()
        self.validate_showcase_description(data)
        self.validate_description(data)
        self.validate_for_resume(data)
        return data

    def save(self, *args, **kwargs):
        education_or_experience = self.cleaned_data['education_or_experience']
        if education_or_experience:
            self.instance.content_object = self._model_for_choice_value(education_or_experience)
        else:
            self.instance.object_id = None
            self.instance.content_type = None
        return super(ProjectForm, self).save(*args, **kwargs)
