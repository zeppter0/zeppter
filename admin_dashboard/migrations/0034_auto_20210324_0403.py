# Generated by Django 3.1.5 on 2021-03-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0033_auto_20210310_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='cat_img'),
        ),
    ]
