# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-25 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeoverapp', '0006_order_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='agent_id',
            field=models.CharField(max_length=1000),
        ),
    ]
