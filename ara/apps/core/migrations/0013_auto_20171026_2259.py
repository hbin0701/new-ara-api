# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='content',
            field=models.TextField(blank=True, verbose_name='내용'),
        ),
    ]
