# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 02:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Course',
        ),
    ]
