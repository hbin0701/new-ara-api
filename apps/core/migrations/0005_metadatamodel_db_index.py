# Generated by Django 2.2.14 on 2020-08-06 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='article',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='articledeletelog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='articledeletelog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='articlereadlog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='articlereadlog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='articleupdatelog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='articleupdatelog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='bestarticle',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='bestarticle',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='bestcomment',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='bestcomment',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='block',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='block',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='board',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='commentdeletelog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='commentdeletelog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='commentupdatelog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='commentupdatelog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='notificationreadlog',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='notificationreadlog',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='report',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='생성 시간'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='삭제 시간'),
        ),
    ]