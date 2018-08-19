# Generated by Django 2.0.5 on 2018-08-03 18:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 18, 27, 27, 269641, tzinfo=utc)),
        ),
    ]
