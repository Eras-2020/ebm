# Generated by Django 3.1.6 on 2021-02-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0017_auto_20210223_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
