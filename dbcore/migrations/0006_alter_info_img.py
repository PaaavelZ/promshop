# Generated by Django 4.2.4 on 2023-09-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0005_info_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка сбоку'),
        ),
    ]
