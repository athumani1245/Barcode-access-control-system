# Generated by Django 3.2.4 on 2021-06-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='programme',
            field=models.CharField(max_length=50),
        ),
    ]