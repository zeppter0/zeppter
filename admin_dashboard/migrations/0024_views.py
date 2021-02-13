# Generated by Django 3.1.5 on 2021-02-10 22:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0023_auto_20210203_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('post_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]