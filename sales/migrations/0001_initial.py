# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Agent')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_no', models.CharField(max_length=50)),
                ('model_type', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Vehicle'),
        ),
    ]
