# Generated by Django 3.2.4 on 2021-06-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_rename_polls_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='name',
        ),
    ]
