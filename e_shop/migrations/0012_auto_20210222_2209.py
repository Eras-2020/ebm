# Generated by Django 3.1.6 on 2021-02-22 19:09

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0011_auto_20210222_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Blog categories',
            },
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image_add',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, default='', upload_to='uploads/images')),
                ('video', models.FileField(blank=True, default='', upload_to='uploads/video')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('blog_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_shop.blogcategory')),
            ],
        ),
    ]
