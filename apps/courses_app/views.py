from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

from django.contrib import messages

def index(request):
	context = {
		"courses": Course.objects.all()
		}
	return render(request, "courses_app/index.html", context)

def delete(request, id):
	context = {
		"courses": Course.objects.filter(id=id)
		}
	return render(request, "courses_app/delete.html", context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
	else:
		def createCourse():
			coursename = request.POST['name']
			coursedesc = request.POST['desc']
			Course.objects.create(name = coursename, desc=coursedesc)
		createCourse()
		return redirect("/")


def destroy(request, id):
	courseid = request.POST['id']
	c = Course.objects.get(id=courseid)
	c.delete()
	return redirect("/")

def comments(request, id):
	context = {
		"comments": Comment.objects.filter(course = Course.objects.filter(id=id))
	}
	return render(request, "courses_app/comments.html", context)

def comment(request):
	comment = request.POST['comment']
	courseid = request.POST['id']
	createdcomment = Comment.objects.create(comment= comment)
	createdcomment.course= courseid
	createdcomment.save()
	return redirect("/comments/"+courseid)