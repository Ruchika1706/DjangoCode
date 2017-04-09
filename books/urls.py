"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#. means current directory
from . import views
#Introduction to namespace, define a namespace here
app_name = 'books'

#define URL pattern for books
#To tell python when we redirect to this, we want to call index() in views file
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #/books/2 (2 is the id)
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name = 'detail'),

]
