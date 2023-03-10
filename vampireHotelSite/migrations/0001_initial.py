# Generated by Django 4.1.7 on 2023-03-10 09:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('passport_series', models.CharField(max_length=4)),
                ('passport_number', models.CharField(max_length=6)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('apartments_type', models.CharField(max_length=20)),
                ('guests_number', models.IntegerField()),
            ],
        ),
    ]
