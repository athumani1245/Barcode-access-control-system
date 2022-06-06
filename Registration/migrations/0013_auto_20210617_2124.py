# Generated by Django 3.2.4 on 2021-06-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0012_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='programme',
            field=models.CharField(choices=[('BIT', 'Bachelor of Science in Information Technology'), ('BAC', 'Bachelor of Accountancy'), ('BAIT', 'Bachelor of Accountancy in Information Technology'), ('BBF', 'Bachelor of Banking and Finance')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE')], max_length=8),
        ),
    ]