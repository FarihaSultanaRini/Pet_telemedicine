# Generated by Django 3.1 on 2021-09-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_name', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField(blank=True)),
                ('degree', models.CharField(max_length=200)),
                ('speciality', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]