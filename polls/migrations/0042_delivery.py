# Generated by Django 2.2.2 on 2019-09-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0041_auto_20190918_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
