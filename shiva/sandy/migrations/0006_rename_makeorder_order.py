# Generated by Django 3.2.9 on 2022-06-12 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sandy', '0005_rename_makeorders_makeorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='makeorder',
            new_name='Order',
        ),
    ]
