# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-19 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=10000)),
                ('phone_number', models.CharField(max_length=1000)),
                ('creator_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1000)),
                ('agent_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=1000)),
                ('category_id', models.IntegerField(default=0)),
                ('brand_id', models.IntegerField(default=0)),
                ('colour', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('phone_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('admin', models.IntegerField(default=0)),
                ('active', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=1000)),
                ('group_id', models.IntegerField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=1000)),
            ],
        ),
    ]
