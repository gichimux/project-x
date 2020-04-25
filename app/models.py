# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import F

DEFAULT_LOCATION_ID = 1
DEFAULT_CUSTOMER_ID = 1
DEFAULT_PRODUCT_ID = 1
DEFAULT_METER_ID = 1

class Product(models.Model):
	product_name = models.CharField(max_length= 12)
	product_price_per_unit = models.PositiveIntegerField(default=0)
	# units_sold = models.PositiveIntegerField(default=0)
	
	def save_product(self):
		self.save()

	def delete_product(self):
		self.delete()

	@classmethod
	def fetch_single_product(cls, product):
		product = cls.objects.get(id=product)
		return product



# # class Receipt(models.Model):
# # 	pass
	

class Location(models.Model):
	zone  = models.CharField(max_length= 10)
	court = models.CharField(max_length= 10)
	house_name = models.CharField(max_length= 10)
	# house_number = models.PositiveIntegerField(default=0)
	# initial_reading = models.PositiveIntegerField(default=0)
	# current_reading = models.PositiveIntegerField(default=0)
	# units_consumed = models.PositiveIntegerField(default=0)
	# date_read = models.DateTimeField(null=True, default=timezone.now)

	# class Meta:
	# 	ordering = ['-id']
    
	def __str__(self):
		return self.house_name 

	def save_location(self):
		self.save()
    
	def delete_location(self):
		self.delete()

	@classmethod
	def fetch_single_location(cls, location):
		location = cls.objects.get(id=location)
		return location

	@classmethod
	def search_location(cls, search_term):
		location = cls.objects.filter(house_name__icontains=search_term)
		return location

	

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length= 10)
    last_name = models.CharField(max_length= 10)
    contact = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location,on_delete=models.CASCADE )
    product = models.ForeignKey(Product,on_delete=models.CASCADE, default=DEFAULT_PRODUCT_ID )
    payment_status = models.BooleanField(default = False)
    # meter_reading = models.ForeignKey('Meter_Reading',default=0)
    # email = models.CharField(max_length= 30,default='email@example.com')


    class Meta:
    	ordering = ['-id']

    def __str__(self):
    	return self.first_name


    def save_customer(self):
    	self.save()

    def delete_customer(self):
    	self.delete()

    @classmethod
    def fetch_all_customers(cls):
    	all_customers = Customer.objects.all()
    	return all_customers

    @classmethod
    def get_customer_by_location(cls, search_term):
    	customer = cls.objects.filter(first_name__icontains =search_term)
    	return customer

    @classmethod
    def get_single_customer(cls, single_customer):
    	single_customer = cls.objects.get(id=single_customer)
    	return single_customer

class Meter_Reading(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=DEFAULT_CUSTOMER_ID)
	# location = models.ForeignKey(Location, on_delete=models.CASCADE, default=DEFAULT_LOCATION_ID)
	previous_reading = models.PositiveIntegerField(default=0)
	current_reading = models.PositiveIntegerField(default=0)
	date_read = models.DateTimeField(null=True, default=timezone.now)

	class Meta:
		ordering = ['-id']
		
	def save_reading(self):
		self.save()

	def delete_reading(self):
		self.delete()

	def units_used(self):
		self.current_reading - self.previous_reading

class Product_details(models.Model):
	product_name = models.CharField(max_length=10)
	product_price = models.PositiveIntegerField(default=0)
	amount_paid = models.PositiveIntegerField(default=0)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=DEFAULT_CUSTOMER_ID )



class Payment_Invoice(models.Model):
	# payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
	date = models.DateTimeField(null=True, default=timezone.now)

	 

class System_User(models.Model):
	first_name = models.CharField(max_length= 10)
	last_name = models.CharField(max_length= 10)
	password = models.CharField(max_length= 10)
	# role = models.ForeignKey("Roles")

# Create your models here.
class Admin(models.Model):
	first_name = models.CharField(max_length= 10)
	last_name = models.CharField(max_length= 10)
	contact = models.CharField(max_length= 10)
	email = models.EmailField(max_length= 254)
	password = models.CharField(max_length= 10)
	licence_code = models.CharField(max_length= 10)

class Enterprise(models.Model):
	enterprise_name = models.CharField(max_length= 10)
	logo = models.ImageField(upload_to='logo_pics',blank=True, height_field=None, width_field=None, max_length=100)
	address = models.CharField(max_length= 10)

class Employees(models.Model):
	user = models.ForeignKey(System_User,on_delete=models.CASCADE)
	user_role = models.CharField(max_length= 10)

class Accounts(models.Model):
	pass
