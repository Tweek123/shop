# Generated by Django 2.2.2 on 2019-09-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20190905_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
