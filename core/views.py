"""User app views"""
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm , SignupForm
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'core/index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'core/contact_form.html'
    success_url = reverse_lazy("core:contact")
    

class SignupView(generic.FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("reviews:list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)