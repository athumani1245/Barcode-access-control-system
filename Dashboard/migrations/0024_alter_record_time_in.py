# Generated by Django 3.2.5 on 2021-07-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0023_alter_record_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time_in',
            field=models.TimeField(null=True),
        ),
    ]