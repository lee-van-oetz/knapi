# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapi', '0002_auto_20170324_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knapsackproblemrequest',
            name='finished',
            field=models.DateTimeField(null=True),
        ),
    ]
