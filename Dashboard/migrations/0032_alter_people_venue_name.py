# Generated by Django 3.2.5 on 2021-08-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0031_alter_people_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='venue_name',
            field=models.CharField(max_length=50),
        ),
    ]
