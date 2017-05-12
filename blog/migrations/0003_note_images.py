# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='images',
            field=models.ImageField(null=True, upload_to=b'img'),
        ),
    ]
