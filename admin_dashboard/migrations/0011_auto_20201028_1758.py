# Generated by Django 3.1.2 on 2020-10-28 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0010_remove_book_book_upload_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_date',
            new_name='book_upload_date',
        ),
    ]