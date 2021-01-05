from django.forms import ModelForm
from .models import Audible

class AudibleForm(ModelForm):
    class Meta:
        model = Audible
        fields = ['book', 'page']