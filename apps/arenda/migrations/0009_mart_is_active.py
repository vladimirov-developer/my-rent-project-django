# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0008_auto_20160701_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='mart',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439'),
            preserve_default=True,
        ),
    ]
