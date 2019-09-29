# Generated by Django 2.2 on 2019-09-28 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0002_event_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='users.CustomUser'),
        ),
    ]