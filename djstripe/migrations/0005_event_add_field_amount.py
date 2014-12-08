# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0004_auto__chg_field_customer_user__add_field_currentsubscription_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='amount',
            field=models.DecimalField(max_digits=8, decimal_places=2, null=True),
            preserve_default=True,
        ),
    ]
