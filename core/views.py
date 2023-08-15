import email
from email import message
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.

def home(request):
    return render(request, 'core/Home.html')

def about(request):
    return render(request, 'core/About.html')

def contact(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # email = request.POST['email']
        # message = request.POST['message'] 
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          name = fm.cleaned_data['name']
          email = fm.cleaned_data['email']
          message=fm.cleaned_data['message']
          reg=User(name=name, email=email, message=message)
          reg.save()
          fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'core/contact.html',{'form':fm})
