# Generated by Django 4.1.5 on 2023-01-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_booking_id_alter_services_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
