# -*- coding: utf-8 -*-

from django.db import models



class Leson(models.Model):
    """Leson Model"""

    class Meta(object):
        verbose_name = u"Предмет"
        verbose_name_plural = u"Предмети"

    lesson_title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назав предмету")



    subscribers = models.ManyToManyField('Student',verbose_name=u"Студенти")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        return u"%s" % (self.lesson_title)

    # def __unicode__(self):
    #     if self.students_selected:
    #         return u"%s (%s %s)" % (self.lesson_title, self.students_selected.first_name,
    #              self.students_selected.last_name,)
    #     else:
    #         return u"%s" % (self.lesson_title,)
