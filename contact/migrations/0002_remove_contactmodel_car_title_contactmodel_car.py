# Generated by Django 4.0.4 on 2022-04-22 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='car_title',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='car',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel', verbose_name='Car'),
            preserve_default=False,
        ),
    ]
