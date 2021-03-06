# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-23 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sx_order', '0003_auto_20190223_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='o_freight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='good_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='o_address',
            field=models.CharField(default='address', max_length=150),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='o_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
