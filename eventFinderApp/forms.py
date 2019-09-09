from django import forms
from .models import Event , Category

class createEvent(forms.ModelForm):
    
    Start_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker7'
        })
    )      

    end_time= forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )      
            
    class Meta:
        model = Event
        fields = ['title','location','description','category']


    def clean(self):
        cleaned_data = super(createEvent, self).clean()
        title = cleaned_data.get('title')
        location = cleaned_data.get('location')
        description = cleaned_data.get('description')
        if not title and not location and not description:
            raise forms.ValidationError('please enter valid input!')
        
