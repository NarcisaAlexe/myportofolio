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


# def cv(request):
#     return render(request, "porto/about.html", {})


def projects(request):
    return render(request, "porto/projects.html", {})


# def pdf_view(request):
#     model = pdf_view
#     template_name = "porto/about.html"
#     success_url = reverse_lazy("curriculum")


# class ContactForm(generic.CreateView):
#     model = Contact()
#     template_name = "contact_form.html"
#     fields = ["name", "email", "message"]
#     success_url = reverse_lazy("contact_form")


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

        # Check if the file is empty and write header
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Name': contact.name, 'Email': contact.email, 'Message': contact.message})


def success(request):
    return HttpResponse('Success!')




# def display_pdf(request):
#     # Specify the path to your HTML file or template
#     html_path = r"C:\Users\Narcisa A\Desktop\myportofolio\porto\templates\porto\about.html"
#
#     # Convert HTML to PDF
#     pdf_content = pdfkit.from_file(html_path, False)
#
#     # Return the PDF response
#     response = HttpResponse(pdf_content, content_type='porto/pdf')
#     response['Content-Disposition'] = 'inline; filename="output.pdf"'
#     return response


def display_pdf(request, pdf_name):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', pdf_name)
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
