# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=300)),
                ('institution', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ATMLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atm', models.OneToOneField(to='market.ATM')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MarketLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.ForeignKey(to='market.Local')),
            ],
        ),
        migrations.CreateModel(
            name='MarketPerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_buy', 'Buyer can buy'), ('can_sell', 'vender can sell')),
            },
        ),
        migrations.CreateModel(
            name='Markets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=300)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarketStand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.ForeignKey(to='market.Markets')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.ForeignKey(to='market.Local')),
                ('parking', models.OneToOneField(to='market.Parking')),
            ],
        ),
        migrations.CreateModel(
            name='Stands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StandVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stand', models.OneToOneField(to='market.Stands')),
            ],
        ),
        migrations.CreateModel(
            name='Translations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.IntegerField()),
                ('add_bonus', models.IntegerField()),
                ('used_bonus', models.IntegerField()),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus', models.IntegerField(null=True, blank=True, default=0)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='translations',
            name='buyer',
            field=models.ForeignKey(to='market.UserProfile'),
        ),
        migrations.AddField(
            model_name='translations',
            name='marketStand',
            field=models.ForeignKey(to='market.MarketStand'),
        ),
        migrations.AddField(
            model_name='standvendor',
            name='vendor',
            field=models.ForeignKey(to='market.UserProfile'),
        ),
        migrations.AddField(
            model_name='marketstand',
            name='stand',
            field=models.OneToOneField(to='market.Stands'),
        ),
        migrations.AddField(
            model_name='marketlocal',
            name='market',
            field=models.OneToOneField(to='market.Markets'),
        ),
        migrations.AddField(
            model_name='atmlocal',
            name='local',
            field=models.ForeignKey(to='market.Local'),
        ),
    ]
