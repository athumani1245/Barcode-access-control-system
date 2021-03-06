# Generated by Django 3.1.7 on 2021-07-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0018_auto_20210618_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
                ('time_in', models.DateTimeField(null=True)),
                ('time_out', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='custodian',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='people',
            name='occupation',
            field=models.CharField(choices=[('1', 'Students'), ('2', 'Staffs'), ('3', 'Visitors')], default='Students', max_length=8),
        ),
    ]
