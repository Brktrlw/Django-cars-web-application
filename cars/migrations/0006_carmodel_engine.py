# Generated by Django 4.0 on 2022-04-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_carmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='engine',
            field=models.CharField(default='', max_length=50, verbose_name='Engine'),
        ),
    ]