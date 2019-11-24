from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event, Category
from django.utils.datastructures import MultiValueDict
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, SplitDateTimeField, ValidationError
from users.models import CustomUser
from django.contrib.admin import widgets


from django.forms import ModelForm, SplitDateTimeField
from .models import Event, Category, Account
from django.contrib.admin import widgets


class createEvent(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ['created_by']
        # fields = ('__all__')
        # widgets = {
        #     'start_time': widgets.AdminSplitDateTime,
        #     'end_time': widgets.AdminSplitDateTime,
        # }


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]

# class createEvent(forms.ModelForm):

    # Category = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(), required=True, )
    # start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    # end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    # # start_time = forms.DateTimeField(
    # #     input_formats=['%d/%m/%Y %H:%M'],
    # #     widget=forms.DateTimeInput(attrs={
    # #         'class': 'form-control datetimepicker-input',
    # #         'data-target': '#datetimepicker7'
    # #     })
    # # )

    # # end_time = forms.DateTimeField(
    # #     input_formats=['%d/%m/%Y %H:%M'],
    # #     widget=forms.DateTimeInput(attrs={
    # #         'class': 'form-control datetimepicker-input',
    # #         'data-target': '#datetimepicker8'
    # #     })
    # # )

    # class Meta:
    #     model = Event
    #     fields = ['title', 'location',
    #               'event_image', 'description', 'start_time', 'end_time']

    # def clean(self):
    #     cleaned_data = super(createEvent, self).clean()
    #     title = cleaned_data.get('title')
    #     location = cleaned_data.get('location')
    #     description = cleaned_data.get('description')
    #     start_time = cleaned_data.get('start_time')
    #     end_time = cleaned_data.get('end_time')
    #     if not title and not location and not description:
    #         raise forms.ValidationError('please enter valid input!')
    #     if start_time > end_time:
    #         raise ValidationError(
    #             'Start time and date must be before end time and date.')

    # def clean_content(self):
    #     content = self.cleaned_data['content']
    #     content_type = content.content_type.split('/')[0]
    #     if content_type in settings.CONTENT_TYPES:
    #         if content._size > settings.MAX_UPLOAD_SIZE:
    #             raise ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
    #                 filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    #     else:
    #         raise ValidationError(_('File type is not supported'))
    #     return content
