# Generated by Django 2.2 on 2019-09-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0009_auto_20190909_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]