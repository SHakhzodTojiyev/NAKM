# Generated by Django 4.0.6 on 2022-07-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tadbirlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tadbirlar',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tadbirlar',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
