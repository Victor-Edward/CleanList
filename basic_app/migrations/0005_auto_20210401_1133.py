# Generated by Django 3.1.7 on 2021-04-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20210329_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='endereço',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='contato',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='nome',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantitade',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tipo_de_produto',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
