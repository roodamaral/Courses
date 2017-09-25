from __future__ import unicode_literals

from django.db import models

import re

class CourseManager(models.Manager):

    def basic_validator(self, postData):
    	errors = {}
    	name=postData['name']
    	desc=postData['desc']
	if len(name) < 5:
		errors["name"] = "Course name should be more than 5 characters!!"
	if len(desc) < 15:
		errors["desc"] = "Description should be more than 15 characters!!"
	return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)            
	objects = CourseManager()

class Comment(models.Model):
	comment = models.CharField(max_length=255)
	course = models.ManyToManyField(Course, related_name="comments")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)            
