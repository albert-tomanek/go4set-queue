# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0002_auto_20160303_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='queue_start',
            new_name='tail',
        ),
    ]
