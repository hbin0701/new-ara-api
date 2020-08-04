# Generated by Django 2.2.14 on 2020-08-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_ara_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='past_user',
            new_name='is_past',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_kaist',
            field=models.BooleanField(default=False, verbose_name='카이스트 인증된 사용자'),
        ),
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together={('nickname', 'is_past', 'deleted_at'), ('uid', 'deleted_at'), ('sid', 'deleted_at')},
        ),
    ]
