from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ "username", "email", "password1","password2",]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.match(r"^[A-Za-z0-9_]+$", username):
            raise ValidationError( "Username can contain only letters, numbers and underscore.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError( "This email is already registered.")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = { "username": "Enter Username", "email": "Enter Email", "password1": "Enter Password", "password2": "Confirm Password",  }
        for name, field in self.fields.items():
            field.widget.attrs.update({ "class": "form-control", "placeholder": placeholders.get(name, ""),})