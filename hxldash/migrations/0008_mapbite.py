# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-10 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hxldash', '0007_auto_20190318_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapBite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayField', models.CharField(max_length=200)),
            ],
        ),
    ]