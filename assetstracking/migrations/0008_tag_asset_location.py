# Generated by Django 3.1.7 on 2021-04-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0007_auto_20210411_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='asset_location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]