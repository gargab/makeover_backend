from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class user(models.Model):
	phone_number=models.CharField(max_length=12, primary_key=True)
	first_name=models.CharField(max_length=1000)
	last_name=models.CharField(max_length=1000)
	admin=models.IntegerField(default=0)
	active=models.IntegerField(default=0)
	email=models.CharField(max_length=1000)
	group_id=models.IntegerField(null=True,blank=True)
	token=models.CharField(max_length=1000,null=True,blank=True)
	created_by=models.CharField(max_length=1000)
	def __str__(self):
		return self.first_name + " " + self.last_name

class group(models.Model):
	name=models.CharField(max_length=1000)
	created_by=models.CharField(max_length=1000, blank=True, null=True)
	def __str__(self):
		return self.name

class categories(models.Model):
	name=models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class brand(models.Model):
	name=models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class product(models.Model):
	product_id=models.CharField(max_length=1000)
	category_id=models.IntegerField(default=0)
	brand_id=models.IntegerField(default=0)
	colour=models.CharField(max_length=1000)
	price=models.IntegerField(default=0)
	def __str__(self):
		return str(self.product_id) + " " + str(self.category_id)

class customer(models.Model):
	name=models.CharField(max_length=1000)
	address=models.CharField(max_length=1000000)
	phone_number=models.CharField(max_length=1000)
	creator_id=models.CharField(max_length=10000)
	group_id=models.IntegerField()
	def __str__(self):
		return self.name + " " + str(self.group_id)

class order(models.Model):
	status=models.CharField(max_length=1000)
	agent_id=models.IntegerField()
	customer_id=models.IntegerField()
	timestamp=models.DateTimeField(default=timezone.now)
	order_value=models.IntegerField()
	def __str__(self):
		return self.customer_id + " " + self.status

class order_products(models.Model):
	product_id=models.IntegerField()
	quantity=models.IntegerField()
	order_id=models.IntegerField()
	def __str__(self):
		return self.product_id + " " + self.order_id
