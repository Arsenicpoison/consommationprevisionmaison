from django.forms import ModelForm
from app.models import Acheter

class AcheterForm(ModelForm):
    
    class Meta:
        model = Acheter
        fields = '__all__'