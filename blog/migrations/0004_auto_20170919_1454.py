# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170919_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post2',
            old_name='post',
            new_name='body',
        ),
    ]
