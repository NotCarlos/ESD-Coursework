# Generated by Django 4.1.4 on 2023-01-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESD_Project', '0004_alter_club_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Club Address'),
        ),
    ]
