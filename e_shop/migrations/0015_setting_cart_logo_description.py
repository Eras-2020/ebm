# Generated by Django 3.1.6 on 2021-02-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0014_setting_company_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='cart_logo_description',
            field=models.CharField(default='Shop with us!!', max_length=200),
        ),
    ]
