# Generated by Django 3.1.2 on 2020-10-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_auto_20201026_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='book_img',
            new_name='cat_img',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='book_title',
            new_name='cat_title',
        ),
    ]
