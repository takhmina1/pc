# Generated by Django 5.0.3 on 2024-04-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='platform',
        ),
    ]