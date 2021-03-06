# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamfieldsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collapse_streamfields', models.BooleanField(default=True)),
                ('pre_selected_colors', models.TextField(blank=True, help_text="Gescheiden kleuren met een ';' (max. 7)", verbose_name='Pre-kleuren')),
                ('google_api_key', models.CharField(help_text='API Key van Google', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
