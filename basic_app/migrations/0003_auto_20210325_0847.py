# Generated by Django 3.1.7 on 2021-03-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20210325_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]