# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20141225_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leson',
            name='subscribers',
            field=models.ManyToManyField(to='students.Student', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(to='students.Leson', verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0438'),
            preserve_default=True,
        ),
    ]
