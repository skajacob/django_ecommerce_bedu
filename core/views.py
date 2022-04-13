"""User app views"""

from django.shortcuts import render
from django.views import generic
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'core/index.html'


class ContactView(generic.FormView):
    #form_class = 
    template_name = 'core/contact.html'