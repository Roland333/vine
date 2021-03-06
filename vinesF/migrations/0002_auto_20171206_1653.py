# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 15:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vinesF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Birthday',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='users',
            name='Last_connection',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Last_connection'),
        ),
        migrations.AddField(
            model_name='users',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='login',
            field=models.CharField(default=django.utils.timezone.now, max_length=25, verbose_name='Login'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=datetime.datetime(2017, 12, 6, 15, 53, 20, 425000, tzinfo=utc), max_length=100, verbose_name='Password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(default=None, max_length=14, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
