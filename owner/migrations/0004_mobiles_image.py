# Generated by Django 4.2.5 on 2023-10-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_alter_mobiles_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiles',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]