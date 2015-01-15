# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20141225_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lesons_selected',
            field=models.ManyToManyField(to='students.Leson', null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0438', blank=True),
            preserve_default=True,
        ),
    ]
