# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0008_auto_20150601_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceproposalreviewer',
            name='nick',
            field=models.CharField(max_length=255, null=True, verbose_name='Nick Name', blank=True),
            preserve_default=True,
        ),
    ]
