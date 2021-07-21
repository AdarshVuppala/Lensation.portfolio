from django.contrib import admin
from django.urls import path
from Portfolio import views 

urlpatterns = [
    path("", views.index, name='Portfolio'),
    path("contact", views.contact, name='contact'),
    path("Gallaries", views.Gallaries, name='Gallaries'),
    path("Socials", views.Socials, name='Socials'),
    path("Weddings", views.Weddings, name='Weddings'),
    path("Events", views.Events, name='Events'),
    path("Photostream", views.Photostream, name='Photostream'),
    path("KidsPhotography", views.KidsPhotography, name='KidsPhotography'),







]
