# Generated by Django 4.1.5 on 2023-01-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesforbooking', '0002_alter_timesforbooking_day_delete_daysforbooking'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesforbooking.timesforbooking'),
        ),
    ]
