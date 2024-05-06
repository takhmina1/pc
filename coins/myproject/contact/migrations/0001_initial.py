# Generated by Django 5.0.3 on 2024-04-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефонный номер')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема сообщения')),
                ('message', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
