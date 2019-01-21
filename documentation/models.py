from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from django import forms
from django.core.validators import MinValueValidator
from smart_selects.db_fields import ChainedManyToManyField
from smart_selects.db_fields import GroupedForeignKey
# from multiselectfield import MultiSelectField
from easy_select2 import select2_modelform


# Create your models h
class Department(models.Model):
	id = models.AutoField(primary_key=True)
	department=models.CharField(blank=False,unique=True,null=True,max_length=40)
	department_description=models.TextField(blank=False,null=True,max_length=300)
	def  __str__(self):
		return self.department

class Project(models.Model):
	id = models.AutoField(primary_key=True)
	department = models.ForeignKey(Department, blank=False,null=True,on_delete=models.CASCADE)
	project=models.CharField(blank=False,max_length=40)
	project_description=models.TextField(blank=False,null=True,max_length=300)
	class Meta:
		unique_together = ('department', 'project')
	def __str__(self):
		return self.project

class Tags(models.Model):
	id = models.AutoField(primary_key=True)
	tag_name=models.CharField(max_length=20,unique=True,null=True,blank=False)
	class Meta:
		verbose_name_plural = 'Tags'
	def __str__(self):
		return self.tag_name


class Document(models.Model):
	id = models.AutoField(primary_key=True)
	author=models.CharField(null=True,max_length=40,blank=False)
	project = GroupedForeignKey(Project, "product",blank=False)
	version=models.CharField(max_length=20,null=True,blank=False)
	tags=models.ManyToManyField(Tags)
	about = HTMLField('About', null = True, blank =False)
	note=models.TextField(null=True, blank= True)
	modified_date_time = models.DateTimeField(auto_now=True)
	created_date_time = models.DateTimeField(auto_now_add=True)
	publish_mode = models.BooleanField(default=True)
	class Meta:
		unique_together = ('project','version')
	def __str__(self):
		return u'%s' % self.project


#class UserModel(models.Model):
 #   user_created = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_created", editable = False, null=True, blank=True)
  #  time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   # user_modified = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_related_modified",editable = False, null=True, blank=True)
    #time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    #class Meta:
     #   abstract = True









	

	


	


