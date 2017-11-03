# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20161230_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translations',
            name='trans_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
