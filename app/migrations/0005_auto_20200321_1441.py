# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-21 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200316_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=10)),
                ('product_price', models.PositiveIntegerField(default=0)),
                ('amount_paid', models.PositiveIntegerField(default=0)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='payment_invoice',
            name='payment',
        ),
        migrations.AddField(
            model_name='location',
            name='units_consumed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
