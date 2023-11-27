# Generated by Django 4.2.5 on 2023-10-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=120, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('specification', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=20)),
                ('storage', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]