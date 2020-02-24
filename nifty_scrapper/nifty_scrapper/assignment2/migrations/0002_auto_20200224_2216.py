# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharablecontent',
            name='username',
        ),
        migrations.AddField(
            model_name='sharablecontent',
            name='snippet_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='sharablecontent',
            index=models.Index(fields=['snippet_url'], name='snippet_url_idx'),
        ),
    ]
