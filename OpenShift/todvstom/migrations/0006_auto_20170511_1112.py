# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todvstom', '0005_auto_20170511_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='ballroom',
            field=models.CharField(default=1, max_length=200, verbose_name='Ballroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rooms',
            name='symph_b',
            field=models.CharField(default=1, max_length=200, verbose_name='Symphony b'),
            preserve_default=False,
        ),
    ]
