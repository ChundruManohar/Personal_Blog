# Generated by Django 5.0.4 on 2024-05-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
