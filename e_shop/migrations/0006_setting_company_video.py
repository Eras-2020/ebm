# Generated by Django 3.1.6 on 2021-02-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0005_auto_20210221_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='company_video',
            field=models.FileField(default='', upload_to='products/'),
        ),
    ]
