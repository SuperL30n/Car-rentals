# Generated by Django 4.2.7 on 2023-11-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_payments_dropoff_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='dropoff_date',
        ),
        migrations.AddField(
            model_name='payments',
            name='number_of_days',
            field=models.IntegerField(default=1),
        ),
    ]
