# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-19 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0070_auto_20180116_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('api_url', models.CharField(max_length=200, verbose_name='\u63a5\u53e3\u5730\u5740')),
                ('api_param', models.CharField(blank=True, max_length=400, null=True, verbose_name='\u63a5\u53e3\u53c2\u6570')),
                ('api_method', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u63a5\u53e3\u8bbf\u95ee\u7c7b\u578b')),
                ('comment', models.CharField(max_length=80, verbose_name='\u8bf4\u660e')),
            ],
        ),
    ]