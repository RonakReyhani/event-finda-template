from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from .models import Event , Category

class createEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','location','start_time','end_time','description','category']
        widgets = {
            'start_time' : DateTimePickerInput(
                attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker7'
                }),
            'end_time' : DateTimePickerInput(
                attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker8'

            }),

        }
        # start_time = forms.DateTimeField(
        #     input_formats=['%d/%m/%Y %H:%M'],
        #     widget=forms.DateTimeInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-target': '#datetimepicker7'
        #     })
        # )    

        # end_time= forms.DateTimeField(
        #     input_formats=['%d/%m/%Y %H:%M'],
        #     widget=forms.DateTimeInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-target': '#datetimepicker8'
        #     })
        # )           
           
    def clean(self):
        cleaned_data = super(createEvent, self).clean()
        title = cleaned_data.get('title')
        location = cleaned_data.get('location')
        description = cleaned_data.get('description')
        if not title and not location and not description:
            raise forms.ValidationError('please enter valid input!')
            
