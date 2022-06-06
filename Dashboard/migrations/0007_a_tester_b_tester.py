# Generated by Django 3.2.4 on 2021-06-15 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_polls'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('A_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='B_tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_Id', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.a_tester')),
            ],
        ),
    ]
