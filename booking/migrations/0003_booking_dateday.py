# Generated by Django 4.1.5 on 2023-01-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='dateday',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
