# Generated by Django 2.2.2 on 2019-09-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190905_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='../static/polls/images/'),
        ),
    ]