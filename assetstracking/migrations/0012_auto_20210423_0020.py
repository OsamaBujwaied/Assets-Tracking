# Generated by Django 3.1.7 on 2021-04-22 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0011_auto_20210423_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='rfid',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
    ]