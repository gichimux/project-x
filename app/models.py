# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length= 10)
    last_name = models.CharField(max_length= 10)
    contact = models.PositiveIntegerField(max_length= 10)
    location = models.ForeignKey('Location',default=0)
    product = models.ForeignKey('Product',default=0)
    # payment = models.ForeignKey('Payment',default=0)
    payment_status models.BooleanField(default=False)
    # meter_reading = models.ForeignKey('Meter_Reading',default=0)
    # email = models.CharField(max_length= 30,default='email@example.com')

    def __str__(self):

class Meter_Reading(models.Model):
	previous_reading = models.CharField(max_length= 10)
	current_reading = moield(max_length= 10)
	customer = models.ForeignKey("Customer")

class Product(models.Model):
	product_name = models.CharField(max_length= 10)
	product_price = models.PositiveIntergerField(default=130)
	units_sold = models.CharField(max_length= 10)

class Payment_Invoice(models.Model):
	payment = models.ForeignKey("Payment")
	date = models.DateTimeField(auto_add_now=True)

class Payment(models.Model):
	product = models.ForeignKey("Product")
	amount_paid = models.PositiveIntergerField(default=0)

class Location(models.Model):
	zone = models.CharField(max_length= 10)
	court = models.CharField(max_length= 10)
	house_name = models.CharField(max_length= 10)
	house_number = models.PositiveIntegerField(default=0)
	 
