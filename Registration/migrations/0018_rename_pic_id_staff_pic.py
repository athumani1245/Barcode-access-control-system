# Generated by Django 3.2.5 on 2021-08-05 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0017_alter_student_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='pic_id',
            new_name='pic',
        ),
    ]
