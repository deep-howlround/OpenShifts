# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_auto_20170407_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='open_shift',
            options={'permissions': (('can_add_date', 'Can add date'),)},
        ),
    ]
