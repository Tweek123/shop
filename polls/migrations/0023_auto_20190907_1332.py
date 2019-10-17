# Generated by Django 2.2.2 on 2019-09-07 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20190907_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='Catalog_id',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='CatalogItem_id',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='CatalogItem_products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_catalogId',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='product',
            name='product_catalogItemId',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='catalog_items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.CatalogItem'),
        ),
    ]