# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
                ('average_review', models.FloatField()),
            ],
        ),
    ]
