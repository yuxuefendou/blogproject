# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 01:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='emile',
            new_name='email',
        ),
    ]