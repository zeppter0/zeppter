# Generated by Django 3.1.3 on 2021-01-07 04:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0004_auto_20210105_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_arrcat',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='book',
            name='book_catid',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
