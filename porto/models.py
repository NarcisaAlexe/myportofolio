from django.db import models
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
# from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
