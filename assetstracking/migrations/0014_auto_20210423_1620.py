# Generated by Django 3.1.7 on 2021-04-23 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0013_auto_20210423_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowing',
            old_name='subscriber_id',
            new_name='subscriber',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='subscriber_id',
            new_name='subscriber',
        ),
        migrations.RenameField(
            model_name='rfid',
            old_name='subscriber_id',
            new_name='subscriber',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='subscriber_id',
            new_name='subscriber',
        ),
    ]