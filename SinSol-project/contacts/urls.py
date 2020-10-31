from django.urls import path
from . import views

urlpatterns = [
  path('', views.contacts, name='contacts'),
  path('contact', views.contact, name='contact'),
]
