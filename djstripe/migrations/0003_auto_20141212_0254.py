# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0002_event_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprocessingexception',
            name='data',
            field=jsonfield.fields.JSONField(null=True, default=None),
        ),
    ]
