# Generated by Django 2.2 on 2019-10-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0002_event_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='created_by',
            new_name='host',
        ),
    ]
