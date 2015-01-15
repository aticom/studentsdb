# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0430\u0432 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
                ('students_selected', models.ManyToManyField(to='students.Student', null=True, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
            },
            bases=(models.Model,),
        ),
    ]
