#Django provides a separate admin interface
from django.contrib import admin
from models import Book
# Register your models here.
admin.site.register(Book)