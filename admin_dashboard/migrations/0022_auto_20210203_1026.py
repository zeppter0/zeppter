# Generated by Django 3.1.5 on 2021-02-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0021_auto_20210203_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
