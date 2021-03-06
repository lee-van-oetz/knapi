# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnapsackProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('task_json', models.TextField()),
                ('task_hash', models.CharField(max_length=8)),
                ('in_knapsack_json', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='KnapsackProblemRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField()),
                ('task_json', models.TextField()),
                ('task_hash', models.CharField(max_length=8)),
                ('knapsack_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapi.KnapsackProblem')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
