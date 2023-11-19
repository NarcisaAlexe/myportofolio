#  Myportofolio
Django - Portofoliu online


## Cuprins

1. [Introducere](#introduction)
2. [Instalare](#installation)
3. [Aplicabilitate](#usage)
4. [Caracteristici](#features)
  * [models](#models)
  * [admin](#admin)
  * [server](#server)
  * [views](#views)
  * [urls](#urls)
  * [templates](#templates)
5. [Formular de contact](#contactform)


## Introducere <a name="introduction"></a>

Pagină web care conține informații legate de activitatea profesională a unei persoane.

## Instalare <a name="installation"></a>

Aplicația poate fi deschisă cu IDE-ul PyCharm și se va rula comanda  python manage.py runserver din Terminal.

Mai apoi putem accesa link-ul cu port-ul care vor apărea în Terminal dacă mesajul primit va fi unul de succes. 
Exemplu: http://127.0.0.1:8000/. La accesarea paginii, vom interacționa cu pagina de start de unde putem vizualiza informațiile.

## Aplicabilitate <a name="usage"></a>

După accesarea link-ului putem naviga pe pagina de start și pe celelalte pagini afișate în partea dreapta, respectiv pagina în care se afla cv-ul, pagina cu proiecte și pagina de contact.
## Caracteristici <a name="features"></a>
### models

Aici se va regasit codul pentru clasa Contact


from django.db import models
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
# from django import forms


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


 
Modelul "Contat" conține câmpurile care vor fi afișate pe pagina de contact și mai apoi transferate către fișierul csv. 
### admin

Am înregistrat modelul în fișierul admin.py pentru a putea fi folosite

from django.contrib import admin
from .models import Contact

admin.site.register(Contact)


 Librăria .models importăm modelul "Contact", din fisierul Models.py și pentru ca modelul să se înregistreze folosim comanda --> admin.site.register(model_name)

### server

Pentru a ne asigura că serverul functionează corect folosim următoarea comandă:

(django_project)$`python manage.py runserver`

* accesam acest ip dintr-un browser http://127.0.0.1:8000/

Va fi afișat mesajul 'The install worked successfully! Congratulations!' care ne va confirma că serverul este funcțional.

### views

În "views" am creat mai mai multe metode:

	from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, request
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Contact
import csv
import pdfkit
from django.http import FileResponse
from django.conf import settings
import os


def index(request):
    return render(request, "porto/index.html", {})


def projects(request):
    return render(request, "porto/projects.html", {})


class ContactView(CreateView):
    model = Contact
    template_name = "porto/contact_form.html"
    fields = ["name", "email", "message"]
    success_url = reverse_lazy("contact_form")

    def form_valid(self, form):
        response = super().form_valid(form)
        write_to_csv(self.object)
        return response


def write_to_csv(contact):
    file_path = 'porto/media/contact_data.csv'
    fieldnames = ['Name', 'Email', 'Message']

    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Name': contact.name, 'Email': contact.email, 'Message': contact.message})


def success(request):
    return HttpResponse('Success!')


def display_pdf(request, pdf_name):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', pdf_name)
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')




* Clasa 'ContactView'  este o clasa în care sunt preluate câmpurle din models.py și adăgate pe pagină, în formularul de contact și este legata de fisierul contact_form.html.
  
* Metoda projects este legată de pagina projects.html

* Metoda write_to_csv face scrierea în fișierul csv adăugânf câmpurile completate din pagina formular de contact.
* Metoda success afișează un mesaj de succes de pe  pagina formular de contact.

* Metoda display_pdf afișează pdf-ul cv-ului de pe  pagina Curriculum.


### urls

 În fișierul urls.py regăsim locația sau URL-ul pe care pagina web va funcționa.


Importăm 'path' din librăria django.url pe care îl vom folosi pentru rutarea adreselor URL. 



### templates

În templates se regăsesc cele 5 fișiere .html, fișierul .js, fișierul .css și imaginile pe care le-am folosit.

 
* about.html conține pagina în care se regăsește cv-ul.
* contat_form.html conține codul html pentru pagina de contact.
* index.html este reprezentat codul html pentru pagina inițiala, pagina de start.
* projects.html  oferă detalii despre pagina unde se regăsesc proiectele
* success.html afișează un mesaj de succes de pe  pagina formular de contact.
* Fișierele .js și .css fac paginile mai aspectuase, micșorează sau afișează bara de navigare pe pagini, iar imaginile sunt afișate în pagini.



## Formular de contact <a name="contactform"></a>

În cadrul paginii formular de contact infornațiile care provin din câmpurile afișate pe pagină sunt colectate și adăugate intr-un fișier .csv.


