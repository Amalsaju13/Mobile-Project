# Generated by Django 4.2.5 on 2023-11-16 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_mobiles_image'),
        ('customer', '0007_alter_orders_expected_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_delivery_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 22, 0, 12, 26, 966913), null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='owner.mobiles'),
        ),
    ]