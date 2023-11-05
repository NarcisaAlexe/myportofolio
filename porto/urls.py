from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.cv, name='curriculum'),
    path('contact_form/', views.ContactForm.as_view(), name='contact_form'),
    path('projects/', views.projects, name='projects'),

]