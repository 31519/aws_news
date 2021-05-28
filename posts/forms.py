
from django import  forms

from .models import Posts

class DateInput(forms.DateInput):
    input_type = 'date'



class PostsForms(forms.ModelForm):
    images = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Posts
        fields = ['category', 'description', 'heading', 'images', 'post_name', 'published_date']
        widgets = {'published_date':DateInput()}

    def __init__(self, *args, **kwargs):
        super(PostsForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'