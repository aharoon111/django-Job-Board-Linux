from django import forms
from .models import Apply

class Appliedfrom(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['appliedjob' , 'name' , 'email' , 'website' , 'cv' , 'coverletter' ]