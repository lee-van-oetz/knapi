# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapi', '0004_auto_20170324_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knapsackproblemrequest',
            name='task_hash',
        ),
        migrations.RemoveField(
            model_name='knapsackproblemrequest',
            name='task_json',
        ),
        migrations.AddField(
            model_name='knapsackproblem',
            name='finished',
            field=models.DateTimeField(null=True),
        ),
    ]