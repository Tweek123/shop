# Generated by Django 2.2.2 on 2019-09-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190905_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='../blog/'),
        ),
    ]
