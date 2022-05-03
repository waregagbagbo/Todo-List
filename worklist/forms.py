from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','complete')
#style form fields
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'complete':forms.CheckboxInput(attrs={'class':''}),       

        }

# create a class and inherit usercreationfrom
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})) 

         
    class Meta:
        model = User
        fields = ('username','firstname','lastname','email','password1','password2')


    def __init__(self, *args, **kwargs):
                super(RegisterUserForm, self).__init__(*args, **kwargs)
        
       # self.fields =['username'].widget.attrs['class'] = 'form-control'
       # self.fields =['password1'].widget.attrs['class'] = 'form-control'
        #self.fields =['paswword2'].widget.attrs['class'] = 'form-control'       

  
  
    
