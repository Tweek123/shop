# Generated by Django 2.2.2 on 2019-09-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_auto_20190907_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='', max_length=60),
        ),
    ]