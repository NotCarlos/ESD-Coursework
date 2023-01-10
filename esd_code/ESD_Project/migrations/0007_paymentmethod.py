# Generated by Django 4.1.4 on 2023-01-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESD_Project', '0006_club_clubnumber_club_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=120, verbose_name='Holder Name')),
                ('cardnumber', models.CharField(max_length=120, verbose_name='Card Number')),
                ('expireydate', models.CharField(max_length=2, verbose_name='Expire Date')),
            ],
        ),
    ]
