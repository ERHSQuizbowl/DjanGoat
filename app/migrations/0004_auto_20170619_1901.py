# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170619_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to='app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='app.User'),
        ),
    ]
