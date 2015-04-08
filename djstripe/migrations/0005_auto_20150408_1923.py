# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_accountlineitemdetail_subscription'),
        ('djstripe', '0004_auto_20150308_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='paypal_customer',
            field=models.ForeignKey(to='billing.PaypalCustomer', null=True),
            preserve_default=True,
        ),
    ]
