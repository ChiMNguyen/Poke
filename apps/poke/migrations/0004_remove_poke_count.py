# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0003_poke_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='count',
        ),
    ]
