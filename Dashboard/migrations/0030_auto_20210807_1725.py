# Generated by Django 3.2.5 on 2021-08-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0029_alter_location_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='class1_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='class1_out',
        ),
        migrations.RemoveField(
            model_name='people',
            name='class2_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='class2_out',
        ),
        migrations.RemoveField(
            model_name='people',
            name='library_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='library_out',
        ),
        migrations.RemoveField(
            model_name='people',
            name='office1_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='office1_out',
        ),
        migrations.RemoveField(
            model_name='people',
            name='office2_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='office2_out',
        ),
        migrations.RemoveField(
            model_name='people',
            name='status_pool',
        ),
        migrations.RemoveField(
            model_name='record',
            name='venue',
        ),
        migrations.AddField(
            model_name='people',
            name='venue_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='venue_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]