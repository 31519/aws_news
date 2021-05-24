from django import forms
from django.forms.widgets import DateInput

from .models import Advertise

class AdvertiseForm(forms.ModelForm):
    adv_start_date = forms.DateField(widget=DateInput)
    adv_end_date = forms.DateField(widget=DateInput)
    

    class Meta:
        model = Advertise
        fields = ['adv_category', 'adv_heading', 'adv_descriptions', 'adv_images', 'adv_conclude']



