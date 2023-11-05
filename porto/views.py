from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from django.urls import reverse_lazy

from .models import Question, Choice, ContactForm, pdf_view
# from .form import UploadCvForm


def index(request):
    # return HttpResponse("Hello!This is my  portofolio.")
    return render(request, "porto/index.html", {})


# class Cv(generic.ListView):
#     template_name = "porto/about.html"
#     context_object_name = "cv"

def cv(request):
    return render(request, "porto/about.html", {})


def projects(request):
    return render(request, "porto/projects.html", {})


class ContactForm(generic.CreateView):
    model = ContactForm
    template_name = "porto/contact_form.html"
    fields = ["first_name", "last_name", "email", "company", "message"]
    success_url = reverse_lazy("contact_form")


def pdf_view(request):
    model = pdf_view
    template_name = "porto/about.html"
    success_url = reverse_lazy("curriculum")


