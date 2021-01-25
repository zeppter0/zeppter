# Generated by Django 3.1.5 on 2021-01-24 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0009_auto_20210107_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='keyboard',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_data',
            field=models.CharField(default='', max_length=100000),
        ),
    ]