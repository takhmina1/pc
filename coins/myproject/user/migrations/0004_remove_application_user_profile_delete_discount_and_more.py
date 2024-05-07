# Generated by Django 5.0.3 on 2024-04-29 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_discount_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='promocode',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='referred',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='referrer',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PromoCode',
        ),
        migrations.DeleteModel(
            name='Referral',
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]