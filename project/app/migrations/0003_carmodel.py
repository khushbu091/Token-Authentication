# Generated by Django 5.0.4 on 2024-04-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employeemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('emyearp_city', models.CharField(max_length=100)),
            ],
        ),
    ]
