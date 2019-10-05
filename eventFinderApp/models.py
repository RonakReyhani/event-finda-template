from django.db import models
# from django.contrib.auth.models import User
from users.models import CustomUser
from django import forms
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import datetime, timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100, default='Description')
    description = models.TextField(
        null=True, help_text="Please add details about your event here")
    start_time = models.DateTimeField('start time and date', null=True)
    end_time = models.DateTimeField('end time and date', null=True)
    category = models.ManyToManyField(
        Category, help_text='Select a category for this event')
    event_image = models.ImageField(upload_to='images/', null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_by')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse('event', args=[str(self.id)])

    @ property
    def get_cat_values(self):
        ret = ''
        print(self.category.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for category in self.category.all():
            ret = ret + category.name + ','
        # remove the last ',' and return the value.
        return ret[:-1]

    def wordcount(self, description):
        """Return the number of words."""
        return len(self.description.split())

    @property
    def is_not_past_event(self):
        return self.start_time >= datetime.now(tz=timezone.utc)


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
