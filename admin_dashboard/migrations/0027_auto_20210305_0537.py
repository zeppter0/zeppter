# Generated by Django 3.1.5 on 2021-03-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0026_auto_20210212_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_data',
            field=models.CharField(default='', max_length=1000000000),
        ),
    ]
