# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='todo_lists',
            field=models.ManyToManyField(to='catalog.TodoList'),
        ),
    ]
