# Generated by Django 4.1.5 on 2023-04-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='0000', max_length=50, verbose_name='Profil Resmi'),
        ),
        migrations.AddField(
            model_name='profile',
            name='password_active',
            field=models.BooleanField(default=False, verbose_name='Şifreyi Etkinleştir'),
        ),
    ]
