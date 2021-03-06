# Generated by Django 3.1 on 2020-11-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201114_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ceremonial', 'Ceremonial'), ('Courtwear', 'Courtwear'), ('Accessories', 'Accessories')], default='Accessories', max_length=20),
        ),
        migrations.RemoveField(
            model_name='product',
            name='other_image',
        ),
        migrations.AddField(
            model_name='product',
            name='other_image',
            field=models.ManyToManyField(blank=True, null=True, to='store.OtherImages'),
        ),
    ]
