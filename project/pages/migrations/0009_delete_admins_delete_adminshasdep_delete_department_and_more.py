# Generated by Django 4.2.1 on 2023-06-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admins',
        ),
        migrations.DeleteModel(
            name='AdminsHasDep',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='search',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserhasDep',
        ),
    ]
