from django import forms
from .models import *

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','complete')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'complete':forms.CheckboxInput(attrs={'class':''}),        

        }