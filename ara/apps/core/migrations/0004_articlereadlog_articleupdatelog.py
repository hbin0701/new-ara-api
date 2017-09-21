# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReadLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_read_log_set', to='core.Article', verbose_name='조회된 게시글')),
                ('read_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_read_log_set', to=settings.AUTH_USER_MODEL, verbose_name='조회자')),
            ],
            options={
                'verbose_name': '게시물 조회 기록',
                'verbose_name_plural': '게시물 조회 기록',
            },
        ),
        migrations.CreateModel(
            name='ArticleUpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=None, null=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(default=None, null=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('content', models.TextField(verbose_name='본문')),
                ('is_content_sexual', models.BooleanField(default=False, verbose_name='성인/음란성 내용')),
                ('is_content_social', models.BooleanField(default=False, verbose_name='정치/사회성 내용')),
                ('use_signature', models.BooleanField(default=True, verbose_name='서명 사용')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_update_log_set', to='core.Article', verbose_name='변경된 게시글')),
                ('parent_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_update_log_set', to='core.Board', verbose_name='게시판')),
                ('parent_topic', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_update_log_set', to='core.Topic', verbose_name='말머리')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_update_log_set', to=settings.AUTH_USER_MODEL, verbose_name='변경된 게시글,')),
            ],
            options={
                'verbose_name': '게시물 변경 기록',
                'verbose_name_plural': '게시물 변경 기록',
            },
        ),
    ]