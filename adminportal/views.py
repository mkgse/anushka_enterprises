from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from edu.forms import LoginForm,AdmDetails,AdmissionDetails
from edu.models import Addmissionform,Admission_Status,Payment,Feedback
from django.urls import reverse

# Create your views here.
def admin_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user =  authenticate(username=uname,password=upass)
        if user.is_superuser:
          login(request, user)
          messages.success(request, 'Congratulations!! You have Succsessfuly Loged In')
          return HttpResponseRedirect('/adminn/admindashboard/')
        else:
          messages.info(request, 'You are not Admin. You can not  Accsess this login Page!!')
  else:
      form = LoginForm()
  return render(request,'adminportal/admin_login.html',{'form':form })
 else:
      return HttpResponseRedirect('/edu/dashboard')
 
def admin_dashboard(request):
    admission_list = Addmissionform.objects.all()
    return render(request,'adminportal/admindashboard.html',{'admission_list':admission_list})

def delete_form(request,id):
   if request.method == 'POST':
      pi = Addmissionform.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect(reverse('admindashboard'))
   
def view_form(request,id):
   if request.method == 'post':
         return render(request, 'adminportal/viewform.html') 
   else:
      form = Addmissionform.objects.get(pk=id)
      return render(request, 'adminportal/viewform.html',{'fm':form}) 
   
def update_form(request,id):
   if request.method == 'POST':
      pi = Addmissionform.objects.get(pk=id)
      fm = AdmDetails(request.POST, instance=pi)
      if fm.is_valid():
         fm.save()
         messages.success(request, 'Your data has been succsessfully Modified !!')
   else:
       pi = Addmissionform.objects.get(pk=id)
       fm = AdmDetails(instance=pi)
   return render(request,'adminportal/updateform.html',{'details':fm})

def admission_status(request):
   form  = Admission_Status.objects.all()
   return render(request,'adminportal/admstatus.html',{'form':form})

def update_status(request,id):
   if request.method == 'POST':
      pt = Admission_Status.objects.get(pk=id)
      fm = AdmissionDetails(request.POST, instance=pt)
      if fm.is_valid():
         fm.save()
         messages.success(request, 'Your data has been succsessfully Modified !!')
   else:
        pt = Admission_Status.objects.get(pk=id)
        fm = AdmissionDetails(instance=pt)
   return render(request,'adminportal/updateadmissionstatus.html',{'form':fm})

def student_payment_details(request):
   form = Payment.objects.all()
   return render(request,'adminportal/studentpayment.html',{'form':form})
def feedback_details(request):
   form=Feedback.objects.all()           
   return render(request,'adminportal/feedbackdetails.html',{'form':form})