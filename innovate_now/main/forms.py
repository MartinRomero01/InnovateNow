from django import forms
from .models import NavbarItem, About, Service

class NavbarItemForm(forms.ModelForm):
    class Meta:
        model = NavbarItem
        fields = ['title', 'url']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']
