# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='best', to='core.Article', verbose_name='문서')),
            ],
            options={
                'verbose_name': '베스트 문서',
                'verbose_name_plural': '베스트 문서',
            },
        ),
        migrations.CreateModel(
            name='BestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='best', to='core.Comment', verbose_name='댓글')),
            ],
            options={
                'verbose_name': '베스트 댓글',
                'verbose_name_plural': '베스트 댓글',
            },
        ),
    ]