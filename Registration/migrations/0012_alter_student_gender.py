# Generated by Django 3.2.4 on 2021-06-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0011_auto_20210617_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6),
        ),
    ]
