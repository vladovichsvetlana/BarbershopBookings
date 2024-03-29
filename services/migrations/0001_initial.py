# Generated by Django 4.1.5 on 2023-01-06 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usermodify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('service', models.TextField()),
                ('about', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodify.usermodify')),
            ],
        ),
    ]
