# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_userpostcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpost',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='userpostcomment',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterField(
            model_name='userpost',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpostcomment',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpostcomment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='socialapp.UserPost'),
        ),
    ]
