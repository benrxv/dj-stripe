# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# import __builtin__
# import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djbraintree', '0002_auto_20150308_1816'),
        ('djstripe', '0003_auto_20141212_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='bt_customer',
            field=models.ForeignKey(to='djbraintree.Customer', null=True),
            preserve_default=True,
        ),
        # migrations.AlterField(
        #     model_name='eventprocessingexception',
        #     name='data',
        #     field=jsonfield.fields.JSONField(default=__builtin__.dict),
        # ),
    ]
