# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0003_auto_20160304_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='head',
            field=models.IntegerField(default=0),
        ),
    ]
