# Generated by Django 3.1.5 on 2021-02-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0006_auto_20210123_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='myueers',
            name='photo',
            field=models.ImageField(default='404_user.png', upload_to='user'),
        ),
    ]
