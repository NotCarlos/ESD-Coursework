# Generated by Django 4.1.4 on 2023-01-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, verbose_name='Username')),
                ('fullname', models.CharField(max_length=200, verbose_name='Fullname')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
        ),
    ]
