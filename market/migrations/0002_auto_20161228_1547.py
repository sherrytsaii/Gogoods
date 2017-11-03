# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standvendor',
            name='stand',
            field=models.OneToOneField(to='market.Stands', related_name='stand_detail'),
        ),
    ]
