from django.db import models
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    title = models.CharField(max_length=80)
    # PDF = models.FileField(upload_to='about/')
    #
    # class Meta:
    #     ordering = ['title']
    #
    # def __str__(self):
    #     return f"{self.title}"


def pdf_view(request):
    with open('D:\PDF.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='porto/pdf')
        response['Content-Disposition'] = 'inline;filename=PDF.pdf'
        return response
    # try:
    #     return FileResponse(open('PDF.pdf', 'rb'), content_type='porto/pdf')
    # except FileNotFoundError:
    #     raise Http404()


class ContactForm(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    message = models.CharField(max_length=500)


    def __str__(self):
        return self.choice_text

