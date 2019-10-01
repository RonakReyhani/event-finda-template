from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event, Category
from django.utils.datastructures import MultiValueDict
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, SplitDateTimeField, ValidationError
from users.models import CustomUser


class M2MSelect(forms.Select):
    def value_from_datadict(self, data, files, name):
        if isinstance(data, (MultiValueDict)):
            return data.getlist(name)
        return data.get(name, None)


class createEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time',
                  'event_image', 'description', 'category']

        start_time = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker7'
            })
        )

        end_time = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker8'
            })
        )

    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time',
                  'event_image', 'description', 'category']

    def clean(self):
        cleaned_data = super(createEvent, self).clean()
        title = cleaned_data.get('title')
        location = cleaned_data.get('location')
        description = cleaned_data.get('description')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if not title and not location and not description:
            raise forms.ValidationError('please enter valid input!')
        if start_time > end_time:
            raise ValidationError(
                'Start time and date must be before end time and date.')

    def clean_content(self):
        content = self.cleaned_data['content']
        content_type = content.content_type.split('/')[0]
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        else:
            raise ValidationError(_('File type is not supported'))
        return content
