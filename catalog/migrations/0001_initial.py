# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the task', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('todo_items', models.ManyToManyField(to='catalog.TodoItem')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='todolist',
            name='users',
            field=models.ManyToManyField(help_text='Share this list with another user...', to='catalog.User'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TodoList'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.User'),
        ),
    ]
