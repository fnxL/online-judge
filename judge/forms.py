from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.fields import ChoiceField
 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class editorForm(forms.Form):
    langs = (
    ('1', 'C++'),
    ('0', 'C'),
    ('2', 'Java'),
    ('3', 'Python'),
    ('4', 'JavaScript'),
    )
 
    language = ChoiceField(widget=forms.Select(attrs={'class':'form-select','id':'lang', 'onChange':'selectMode()', 'style':'width:auto;margin-bottom:12px;'}), choices=langs, label='')
    sourcecode = forms.CharField(widget=forms.Textarea(attrs={'id':'source'}), label='')
   
    
 
