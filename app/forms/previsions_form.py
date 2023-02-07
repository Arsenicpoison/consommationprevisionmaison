from django.forms import ModelForm
from app.models import Prevision

class PrevisionForm(ModelForm):
    
    class Meta:
        model = Prevision
        fields = '__all__'