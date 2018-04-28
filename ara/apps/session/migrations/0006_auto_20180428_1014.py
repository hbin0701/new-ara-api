# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-28 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_auto_20180410_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='', upload_to='user_profiles/pictures', verbose_name='프로필'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='signature',
            field=models.TextField(blank=True, default='', verbose_name='서명'),
        ),
    ]
