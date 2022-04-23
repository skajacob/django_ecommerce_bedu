"""User app views"""
from django.core.mail import send_mail
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm , SignupForm
from django.conf import settings
from django.contrib import messages
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'core/index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'core/contact_form.html'
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        messages.info(
            self.request, "We receive your message")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Message received from {name}, {email}
        ______________________________________


        {message}
        """
        send_mail(
            subject="Message receive from Constact Form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
            )
        return super(ContactView, self).form_invalid(form)
    

class StoresView(generic.TemplateView):
    template_name = 'core/stores.html'

class SignupView(generic.FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("reviews:list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)