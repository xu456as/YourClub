# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-05 16:21
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan', to=settings.AUTH_USER_MODEL, verbose_name='\u5173\u6ce8\u8005')),
                ('idol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idol', to=settings.AUTH_USER_MODEL, verbose_name='\u88ab\u5173\u6ce8\u8005')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5173\u6ce8',
                'verbose_name_plural': '\u7528\u6237\u5173\u6ce8',
            },
        ),
    ]