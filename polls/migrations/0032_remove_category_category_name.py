# Generated by Django 2.2.2 on 2019-09-07 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_remove_category_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
    ]
