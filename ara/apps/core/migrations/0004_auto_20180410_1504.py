# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20171125_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrap',
            old_name='article',
            new_name='parent_article',
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set([('parent_article', 'reported_by', 'deleted_at'), ('parent_comment', 'reported_by', 'deleted_at')]),
        ),
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together=set([('parent_article', 'scrapped_by', 'deleted_at')]),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('parent_article', 'created_by', 'deleted_at'), ('parent_comment', 'created_by', 'deleted_at')]),
        ),
    ]
