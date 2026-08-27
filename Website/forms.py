from django import forms
from captcha.fields import CaptchaField
from .models import Contact

class Contact_Form (forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__" 