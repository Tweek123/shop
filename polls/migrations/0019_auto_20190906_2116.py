# Generated by Django 2.2.2 on 2019-09-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20190905_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_descr',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
