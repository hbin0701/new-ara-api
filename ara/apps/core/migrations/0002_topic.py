# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('ko_name', models.CharField(max_length=32, unique=True, verbose_name='말머리 국문 이름')),
                ('en_name', models.CharField(max_length=32, unique=True, verbose_name='말머리 영문 이름')),
                ('ko_description', models.TextField(verbose_name='말머리 국문 소개')),
                ('en_description', models.TextField(verbose_name='말머리 영문 소개')),
                ('parent_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_set', to='core.Board', verbose_name='상위 게시판')),
            ],
            options={
                'verbose_name': '말머리',
                'verbose_name_plural': '말머리',
            },
        ),
    ]