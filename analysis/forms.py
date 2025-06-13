from django import forms
from .models import WaterNetwork

class NetworkUploadForm(forms.ModelForm):
    class Meta:
        model = WaterNetwork
        fields = ['name', 'file']

