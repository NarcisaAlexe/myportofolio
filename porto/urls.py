from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import display_pdf

urlpatterns = [
    path('', views.index, name='index'),
    path('pdfs/<str:pdf_name>/', display_pdf, name='display_pdf'), # http://localhost:8000/pdfs/ex.pdf/
    path('contact_form/', views.ContactView.as_view(), name='contact_form'),
    path('projects/', views.projects, name='projects'),
    path('success/', views.success, name='success')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)