from django.db import models
from django import forms
from django.urls import reverse
from django.core.exceptions import ValidationError
import datetime

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('user-profile', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True,help_text="Please add details about your event here")
    start_time = models.DateTimeField('start time and date',null=True )
    end_time = models.DateTimeField('end time and date',null=True)
    category = models.ManyToManyField(Category ,help_text='Select a category for this event')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse('event', args=[str(self.id)])  

    def get_cat_values(self):
        ret = ''
        print(self.category.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for category in self.category.all():
            ret = ret + category.name + ','
        # remove the last ',' and return the value.
        return ret[:-1]



class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )       
# def present_or_future_date(value):
#         if value < datetime.date.today():
#             raise ValidationError("The event date cannot be in the past!")
#         return value

# def end_before_start(value1,value2):
#     if value2 < value1:
#         raise ValidationError("The End date cannot be before event start time ") 
#     return value2

    

