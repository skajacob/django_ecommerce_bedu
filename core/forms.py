"""Users forms"""

from urllib import request
from django import forms


from core.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Your Name"})) 
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Your Email"}))
    message = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'placeholder':"Your Message"}))

class SignupForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password_confirmation = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user_exist = User.objects.filter(username=username).exists()
        if user_exist:
            raise forms.ValidationError("The Username already exist!!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_exists = User.objects.filter(email=email).exists()
        if email.exists:
            raise forms.ValidationError("This email is already in use!!")
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_cofirmation = self.cleaned_data.get('password_cofirmation')

        if password != password_cofirmation:
            raise forms.ValidationError("The passwords don't match!!")

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        return User.objects.create_user(**data)