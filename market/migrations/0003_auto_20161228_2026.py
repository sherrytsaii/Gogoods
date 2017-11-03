# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20161228_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmlocal',
            name='atm',
            field=models.OneToOneField(related_name='ATM_detail', to='market.ATM'),
        ),
        migrations.AlterField(
            model_name='marketlocal',
            name='market',
            field=models.OneToOneField(related_name='market_detail', to='market.Markets'),
        ),
        migrations.AlterField(
            model_name='marketstand',
            name='stand',
            field=models.OneToOneField(related_name='standM_detail', to='market.Stands'),
        ),
        migrations.AlterField(
            model_name='parkinglocal',
            name='parking',
            field=models.OneToOneField(related_name='parking_detail', to='market.Parking'),
        ),
        migrations.AlterField(
            model_name='standvendor',
            name='stand',
            field=models.OneToOneField(related_name='standV_detail', to='market.Stands'),
        ),
    ]
