# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 22:10
from __future__ import unicode_literals

import apps.core.models.notification
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_articlereadlog_articleupdatelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('data', django_mysql.models.JSONField(default=apps.core.models.notification.get_default_data, verbose_name='알림 JSON')),
                ('notification_type', models.CharField(choices=[('default', 'default')], max_length=256, verbose_name='알림 타입')),
            ],
            options={
                'verbose_name': '알림',
                'verbose_name_plural': '알림',
            },
        ),
    ]