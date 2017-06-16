# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keymanagement',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='paidtimeoff',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='pay',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='performance',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='retirement',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='workinfo',
            old_name='user_id',
            new_name='user',
        ),
    ]