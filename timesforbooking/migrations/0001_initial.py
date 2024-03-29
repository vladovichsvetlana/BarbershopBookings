# Generated by Django 4.1.5 on 2023-01-11 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaysForBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, ' Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='TimesForBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtime', models.TimeField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesforbooking.daysforbooking')),
            ],
        ),
    ]
