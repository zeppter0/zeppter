# Generated by Django 3.1.3 on 2021-01-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0008_auto_20210107_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_data',
            field=models.CharField(max_length=100000),
        ),
    ]
