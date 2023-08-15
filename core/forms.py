from django import forms
from .models import User
from django.core import validators


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields=['name','email','message']
        widgets={

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'message': forms.Textarea(attrs={'class':'form-control','style':'width=300px','placeholder':'Type Here Some else here..'}),
        }

        error_messages={
            'name':{'required':'Enter the Name'},
            'email':{'required':'Enter the Email'}
        }