from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('about', views.about, name='about'),

]
