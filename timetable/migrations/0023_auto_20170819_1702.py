# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-19 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0022_auto_20170819_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='author',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='detail_url',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='title',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]