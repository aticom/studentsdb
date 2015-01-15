# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20141225_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leson',
            old_name='students_selected',
            new_name='subscribers',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(to='students.Leson', null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0438', blank=True),
            preserve_default=True,
        ),
    ]
