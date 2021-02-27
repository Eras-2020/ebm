# Generated by Django 3.1.6 on 2021-02-24 18:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0023_auto_20210224_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='cart_logo',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='cart_logo_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Shop with us!!'),
        ),
    ]