# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-11 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0017_task_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='svn_url',
            field=models.TextField(blank=True, null=True, verbose_name='SVN\u8def\u5f84'),
        ),
    ]
