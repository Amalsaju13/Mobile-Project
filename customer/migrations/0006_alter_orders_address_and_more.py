# Generated by Django 4.2.5 on 2023-11-16 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_orders_expected_delivery_date_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 21, 22, 43, 4, 161161), null=True),
        ),
    ]
