# from __future__ import unicode_literals
# from django.db import models
#
# class User(models.Model):
#     admin = models.BooleanField(default=True)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Product(models.Model):
#     item_name = models.CharField(max_length=255)
#     desc = models.TextField(null=True, blank=True)
#     price = models.IntegerField(default=0)
#     the_user = models.ForeignKey(User, related_name='products')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
