from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
    admin = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    address_two = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=80)
    # billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name + ' | ' + self.last_name + ' | ' + self.email

class Product(models.Model):
    product = models.CharField(max_length=60)
    price = models.IntegerField()
    weight = models.IntegerField()
    quantity = models.IntegerField()
    buyers = models.ManyToManyField(User, related_name = 'products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job  + ' | '

class Species(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=700)
    impact = models.TextField(max_length=700)
    product = models.ForeignKey(Product, related_name='species_info')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def __str__(self):
        return self.name  + ' | ' + self.description
