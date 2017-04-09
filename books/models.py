#to create database or database tables so that site has relevant data
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# First define the structure of database
class Book(models.Model): #Creating a book table here
    name = models.CharField(max_length = 100) # Character field of maximum length 100
    author = models.CharField(max_length = 100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name + '-' + self.author

#Create a new table here if you want
class table_name(models.Model):
    pass
