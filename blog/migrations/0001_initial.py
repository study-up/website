# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, unique=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'published', b'Published')])),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
