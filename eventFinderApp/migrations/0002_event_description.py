# Generated by Django 2.2 on 2019-09-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Please add details about your event here', null=True),
        ),
    ]