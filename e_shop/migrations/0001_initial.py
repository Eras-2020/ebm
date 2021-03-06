# Generated by Django 3.1.6 on 2021-02-17 18:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('in_stock', models.IntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(blank=True, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')], max_length=100)),
                ('quantity', models.CharField(blank=True, choices=[('1/2Kg', '1/2Kg'), ('1Kg', '1Kg'), ('1/2L', '1/2L'), ('1L', '1L')], max_length=100)),
                ('color', models.CharField(choices=[('Blue', 'Blue'), ('Black', 'Black'), ('Red', 'Red'), ('White', 'White'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Green', 'Green'), ('Gray', 'Gray')], max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='products/')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('delivery_time', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_shop.category')),
            ],
        ),
    ]
