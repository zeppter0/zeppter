# Generated by Django 3.1.3 on 2021-01-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0007_auto_20210107_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_catid',
            field=models.IntegerField(default=1),
        ),
    ]