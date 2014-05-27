from django.forms import ModelForm
from home.models import Citas
from django.contrib.auth.models import User

class CitaForm(ModelForm):
    class Meta:
        model = Citas

class RegistroForm(ModelForm):
    class Meta:
        model = User
        
