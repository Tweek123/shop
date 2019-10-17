# Generated by Django 2.2.2 on 2019-09-07 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_remove_category_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(default='', max_length=60)),
                ('product_descr', models.CharField(default='', max_length=200)),
                ('product_price', models.CharField(default='', max_length=200)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_categories', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
        ),
    ]