# Generated by Django 3.1 on 2020-10-25 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201025_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
    ]
