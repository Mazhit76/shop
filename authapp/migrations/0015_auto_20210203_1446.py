# Generated by Django 3.1.5 on 2021-02-03 11:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_auto_20210203_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 11, 46, 33, 629820, tzinfo=utc)),
        ),
    ]