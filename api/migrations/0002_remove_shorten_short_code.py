# Generated by Django 5.1.1 on 2024-10-06 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorten',
            name='short_code',
        ),
    ]
