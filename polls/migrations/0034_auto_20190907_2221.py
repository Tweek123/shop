# Generated by Django 2.2.2 on 2019-09-07 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_product1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_catalog',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_categories',
        ),
        migrations.RemoveField(
            model_name='product1',
            name='product_categories',
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Product1',
        ),
    ]