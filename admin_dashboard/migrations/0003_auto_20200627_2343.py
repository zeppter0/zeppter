# Generated by Django 3.0.7 on 2020-06-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0002_auto_20200606_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='', upload_to='book_img'),
        ),
    ]
