# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-14 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_userregistry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='UserProfile/default.png', upload_to='UserProfile/%Y/%m'),
        ),
    ]