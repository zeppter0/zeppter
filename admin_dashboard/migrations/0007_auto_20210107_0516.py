# Generated by Django 3.1.3 on 2021-01-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_auto_20210107_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_data',
            field=models.CharField(default=None, max_length=100000),
        ),
    ]
