# Generated by Django 4.1.4 on 2023-01-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESD_Project', '0007_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='cardnumber',
            field=models.CharField(max_length=16, verbose_name='Card Number'),
        ),
    ]
