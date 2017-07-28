# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0003_auto_20170728_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
