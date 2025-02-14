# Generated by Django 4.2.7 on 2023-11-29 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=255)),
                ('car_type', models.CharField(max_length=255)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('brief_description_of_the_car', models.TextField(max_length=1024)),
                ('car_category', models.CharField(max_length=255)),
                ('no_of_seats', models.IntegerField(blank=True, default=1, null=True)),
                ('amount_per_day', models.FloatField(default=5000)),
                ('car_availability', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('email_address', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=1024)),
                ('address', models.CharField(max_length=2555)),
                ('town_city', models.CharField(max_length=1025)),
                ('pickup_location', models.CharField(max_length=2555)),
                ('pickup_date', models.DateField()),
                ('dropoff_location', models.CharField(max_length=2555)),
                ('payment_ref', models.CharField(default='', max_length=255)),
                ('number_of_days', models.IntegerField(default=1)),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('car_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.car')),
            ],
        ),
    ]
