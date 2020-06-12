# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='color',
            field=models.CharField(default=b'black', max_length=10, null=True),
        ),
    ]
