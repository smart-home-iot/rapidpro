# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 17:09
from __future__ import absolute_import, division, print_function, unicode_literals
from django.db import migrations


def cleanup_dependencies(apps, schema_editor):
    ContactField = apps.get_model('contacts', 'ContactField')
    Flow = apps.get_model('flows', 'Flow')

    flow_ids = ContactField.objects.filter(dependent_flows__is_active=False).distinct('dependent_flows__id').values_list('dependent_flows__id')
    for flow in Flow.objects.filter(id__in=flow_ids, is_active=False):
        flow.field_dependencies.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0117_auto_20171027_2029'),
    ]

    operations = [
        migrations.RunPython(cleanup_dependencies)
    ]