# Generated by Django 3.2.5 on 2021-08-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0028_alter_location_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='color',
            field=models.CharField(max_length=50),
        ),
    ]
