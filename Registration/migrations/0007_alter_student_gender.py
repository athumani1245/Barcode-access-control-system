# Generated by Django 3.2.4 on 2021-06-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_alter_student_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
