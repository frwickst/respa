# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0029_add_reservation_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='billing_address_city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Billing address city'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='billing_address_street',
            field=models.CharField(blank=True, max_length=100, verbose_name='Billing address street'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='billing_address_zip',
            field=models.CharField(blank=True, max_length=30, verbose_name='Billing address zip'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='business_id',
            field=models.CharField(blank=True, max_length=9, verbose_name='Business ID'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='company',
            field=models.CharField(blank=True, max_length=100, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='event_description',
            field=models.TextField(blank=True, verbose_name='Event description'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='number_of_participants',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of participants'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver_address_city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reserver address city'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver_address_street',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reserver address street'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver_address_zip',
            field=models.CharField(blank=True, max_length=30, verbose_name='Reserver address zip'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reserver name'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver_phone_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='Reserver phone number'),
        ),
    ]