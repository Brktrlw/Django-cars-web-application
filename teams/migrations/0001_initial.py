# Generated by Django 4.0.4 on 2022-04-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('designation', models.CharField(max_length=100, verbose_name='Designation')),
                ('facebook', models.URLField(max_length=100, verbose_name='Facebook Link')),
                ('twitter', models.URLField(max_length=100, verbose_name='Twitter Link')),
                ('google', models.URLField(max_length=100, verbose_name='Google Link')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('image', models.ImageField(upload_to='teams/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
                'db_table': 'TeamMembers',
            },
        ),
    ]
