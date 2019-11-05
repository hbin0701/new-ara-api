# Generated by Django 2.2.5 on 2019-09-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='name',
        ),
        migrations.AddField(
            model_name='attachment',
            name='mimetype',
            field=models.CharField(
                default='text/plain',
                max_length=50,
                verbose_name='타입'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='size',
            field=models.BigIntegerField(
                default=-1,
                verbose_name='용량'),
        ),
    ]
