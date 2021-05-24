from django import forms
from django.forms import fields
from .models import Signup
class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type":"email",
        "name":"email",
        "id":"email",
        "placeholder":"Type your email here "
    }), label="")
    class Meta:
        model = Signup
        fields = ['email']