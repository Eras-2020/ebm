# Generated by Django 3.1.6 on 2021-02-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0024_auto_20210224_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_stock_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
