# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20171227_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the task', max_length=1000, null=True),
        ),
    ]
