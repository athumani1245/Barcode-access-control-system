# Generated by Django 3.2.4 on 2021-06-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_a_tester_b_tester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b_tester',
            name='B_Id',
        ),
        migrations.RemoveField(
            model_name='b_tester',
            name='name',
        ),
    ]
