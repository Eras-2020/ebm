# Generated by Django 3.1.6 on 2021-02-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
