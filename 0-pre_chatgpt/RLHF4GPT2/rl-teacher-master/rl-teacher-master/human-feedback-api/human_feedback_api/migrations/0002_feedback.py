# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-29 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import human_feedback_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('human_feedback_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=b'date created')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('media_path_1', models.TextField(db_index=True, verbose_name=b'media path #1 (left)')),
                ('media_path_2', models.TextField(db_index=True, verbose_name=b'media path #2 (right)')),
                ('tasker_slack_name', models.TextField(db_index=True, verbose_name=b'The slack name of the tasker (without the @)')),
                ('shown_to_tasker_at', models.DateTimeField(db_index=True, verbose_name=b'date created')),
                ('responded_at', models.DateTimeField(db_index=True, verbose_name=b'date created')),
                ('response_kind', models.TextField(db_index=True, validators=[human_feedback_api.models.validate_inclusion_of_response_kind], verbose_name=b'the response from the tasker')),
                ('response', models.TextField(db_index=True, verbose_name=b'the response from the tasker')),
                ('metadata_json', models.TextField(verbose_name=b'json encoded string with metadata')),
            ],
        )
    ]