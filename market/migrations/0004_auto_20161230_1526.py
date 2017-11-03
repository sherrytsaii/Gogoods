# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20161228_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketperm',
            options={'permissions': (('can_buy', 'Buyer can buy'), ('can_sell', 'vendor can sell'))},
        ),
        migrations.AddField(
            model_name='translations',
            name='trans_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
