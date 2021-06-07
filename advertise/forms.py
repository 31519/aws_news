from django import forms
from django.forms.widgets import DateInput

from .models import Advertise, Ads_Payment


# class AdsPaymentForm(forms.ModelForm):

#     class Meta:
#         model = Ads_Payment
#         fields = ['adv_plan']


class DateInput(forms.DateInput):
    input_type = 'date'

class AdvertiseForm(forms.ModelForm):
    adv_images = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Advertise
        fields = ['adv_category', 'adv_heading', 'adv_descriptions', 'adv_images', 'adv_start_date', 'adv_end_date', 'adv_plan']
        widgets = {'adv_start_date': DateInput(),
                    'adv_end_date': DateInput()
        }
        # widgets = {'adv_end_date': DateInput()}

    def __init__(self, *args, **kwargs):
        super(AdvertiseForm, self).__init__(*args, **kwargs)
        self.fields['adv_category'].widget.attrs['placeholder'] = 'Enter Category'
        self.fields['adv_heading'].widget.attrs['placeholder'] = 'Enter Title'
        self.fields['adv_descriptions'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['adv_images'].widget.attrs['placeholder'] = 'Enter Images'
        # self.fields['adv_end_date'].widget.attrs['class'] = 'form-control'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



# 