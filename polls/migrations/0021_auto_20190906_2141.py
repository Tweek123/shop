# Generated by Django 2.2.2 on 2019-09-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20190906_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
