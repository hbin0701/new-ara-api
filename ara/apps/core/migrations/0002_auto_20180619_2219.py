# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-19 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='use_signature',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='use_signature',
        ),
    ]