# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_start', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='VisitCounter',
        ),
    ]