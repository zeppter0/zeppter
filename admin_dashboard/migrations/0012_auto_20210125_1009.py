# Generated by Django 3.1.5 on 2021-01-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0011_auto_20210125_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(default=None, max_length=150),
        ),
    ]