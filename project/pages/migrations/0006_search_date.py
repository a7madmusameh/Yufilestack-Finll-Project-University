# Generated by Django 4.2.1 on 2023-06-02 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
