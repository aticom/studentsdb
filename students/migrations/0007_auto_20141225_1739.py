# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_lesons_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='lesons_selected',
        ),
        migrations.AlterField(
            model_name='leson',
            name='students_selected',
            field=models.ManyToManyField(to='students.Student', null=True, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438', blank=True),
            preserve_default=True,
        ),
    ]
