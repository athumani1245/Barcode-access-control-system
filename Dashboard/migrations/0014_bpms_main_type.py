# Generated by Django 3.2.4 on 2021-06-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0013_bpms_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpms_main',
            name='type',
            field=models.CharField(default='student', max_length=8),
        ),
    ]
