# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/piv.png'},
    )
    return render(request, 'students/students_list.html',
        {'students': students})


def students_add(request):
    return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
