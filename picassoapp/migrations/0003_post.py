# Generated by Django 2.1.7 on 2019-03-16 01:58

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('picassoapp', '0002_auto_20190313_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
    ]