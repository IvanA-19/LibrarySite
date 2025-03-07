# Generated by Django 5.1.4 on 2024-12-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=300, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=300, verbose_name='Фамилия')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/user_avatars', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
