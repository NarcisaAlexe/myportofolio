from django import forms
from .models import Contact


# class ContactForm(forms.ModelForm):
class ContactForm(forms.Form):
        name = forms.CharField(max_length=100)
        email = forms.EmailField()
        message = forms.CharField(widget=forms.Textarea)

