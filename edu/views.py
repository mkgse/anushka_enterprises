from django.shortcuts import render , HttpResponseRedirect,redirect
from .forms import SignUpForm , LoginForm,ChangeForm,AdmDetails,PaymentDetails,FeedbackForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .models import Payment,Addmissionform,Admission_Status,Feedback
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Home(request):

  if not request.user.is_authenticated:
   if request.method == 'POST':
 
    return render(request,'edu/Index.html')
   else:
        return render(request,'edu/Index.html')
  else:
     user = request.user
     full_name = user.get_full_name()
     return render(request,'edu/Index.html',{'full_name':full_name})
  

def about1(request):
    return render(request,'edu/about1.html')
def admission(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user =  authenticate(username=uname,password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Congratulations!! You have Succsessfuly Loged In')
        return HttpResponseRedirect('/edu/admissionform')
  else:
      form = LoginForm()
  return render(request,'edu/admission.html',{'form':form })
 else:
      return HttpResponseRedirect('/edu/dashboard')
def course(request):
    return render(request,'edu/course.html')


def sign_up(request):
    if request.method == "POST":
     fm = SignUpForm(request.POST)
     if fm.is_valid():
       messages.success(request, 'Congratulations!! You have Succsessfuly Registerd')
                
       user = fm.save()
       fm = SignUpForm()
       return HttpResponseRedirect('/edu/admission')
    else:
     fm = SignUpForm()
    return render(request,'edu/signup.html',{'form':fm})
def user_change_pass(request):
  if  request.user.is_authenticated:
    if request.method == "POST":
        form = ChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, 'Your Password has been Succsessfuly Changed !')
        return render(request, 'edu/changepass.html',{'form':form})
    else:
       user = request.user
       full_name = user.get_full_name()
       form = ChangeForm(user=request.user)
       return render(request, 'edu/changepass.html',{'form':form,'full_name':full_name})
  else:
    return HttpResponseRedirect('/edu/admission')
   

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/edu/admission')

    #education form

def admission_details(request):
   if request.user.is_authenticated:
    if request.method == 'POST':
      details = AdmDetails(request.POST, request.FILES)
      if details.is_valid():
         usr = request.user
         firstname = details.cleaned_data['firstname']
         middlename = details.cleaned_data['middlename']
         lastname = details.cleaned_data['lastname']
         fathername = details.cleaned_data['fathername']
         mothername = details.cleaned_data['mothername']
         dob =details.cleaned_data['dob']
         gender = details.cleaned_data['gender']
         mobile = details.cleaned_data['mobile']
         email = details.cleaned_data['email']
         address = details.cleaned_data['address']
         city = details.cleaned_data['city']
         state = details.cleaned_data['state']
         pin = details.cleaned_data['pin']
         board = details.cleaned_data['board']
         board1 = details.cleaned_data['board1']
         board2 = details.cleaned_data['board2']
         passing_year = details.cleaned_data['passing_year']
         passing_year1 = details.cleaned_data['passing_year1']
         passing_year2 = details.cleaned_data['passing_year2']
         percentage = details.cleaned_data['percentage']
         percentage1 = details.cleaned_data['percentage1']
         percentage2 = details.cleaned_data['percentage2']
         roll_number = details.cleaned_data['roll_number']
         roll_number1 = details.cleaned_data['roll_number1']
         roll_number2 = details.cleaned_data['roll_number2']
         photo = details.cleaned_data['photo']
         signature = details.cleaned_data['signature']
         matriculation = details.cleaned_data['matriculation']
         intermediate = details.cleaned_data['intermediate']
         graducation = details.cleaned_data['graducation']
         postgraducation = details.cleaned_data['postgraducation']
         address_proof = details.cleaned_data['address_proof']
         course_applied_for = details.cleaned_data['course_applied_for']
         reg =Addmissionform(user=usr,firstname=firstname,middlename=middlename,lastname=lastname,fathername=fathername,mothername=mothername
          ,dob=dob,gender=gender,mobile=mobile,email=email,address=address,city=city,state=state,pin=pin,board=board,board1=board1
          ,board2=board2,passing_year=passing_year,passing_year1=passing_year1,passing_year2=passing_year2,percentage=percentage,percentage1=percentage1,percentage2=percentage2
          ,roll_number=roll_number,roll_number1=roll_number1,roll_number2=roll_number2,photo=photo,signature=signature,
          matriculation=matriculation,intermediate=intermediate,graducation=graducation,postgraducation=postgraducation,address_proof=address_proof,
          course_applied_for=course_applied_for)
         reg.save()
         messages.success(request, 'Your Admission Form has been Succsessfully Submited !')
      return HttpResponseRedirect('/edu/printform',{'details':details})
    else:
       user = request.user
       full_name = user.get_full_name()
       user_name = user.get_username()
       details = AdmDetails()
       form = Addmissionform.objects.filter(user=user)
       return render(request, 'edu/admissionform.html',{'details':details,'full_name':full_name,'user':user_name,'form':form})
   else:
       return HttpResponseRedirect('/edu/admission')


def Admission_Details(request):
     if request.user.is_authenticated: 
      if request.method == 'POST':
         return render(request, 'edu/preview.html')
      else:
       user =request.user
       print(user)
       form = Addmissionform.objects.filter(user=user)
       print(form)
       full_name = user.get_full_name()
       return render(request,'edu/preview.html',{'full_name':full_name,'form':form})
     else:
         return HttpResponseRedirect('/edu/admission')
def payment_details(request):
   if request.user.is_authenticated:
      user = request.user
      if request.method == 'POST':
        amount = int(request.POST.get("amount")) * 100
        print(amount)
        client = razorpay.Client(auth=("rzp_test_ugBbbb0MY8YfMB","KSFeqtlQkQFJ1kCblDsUzPGF"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        pdetails = Payment(user=user, amount = amount,paymentid = payment['id'])
        pdetails.save()
        print(payment)
        return render(request,'edu/payment.html',{'payment':payment})
      
      return render(request,'edu/payment.html')
   else:
      return HttpResponseRedirect('/edu/admission')  
   
def Admission_status(request):
   user =request.user
   admstatus = Admission_Status.objects.filter(user=user)
   print(admstatus)
   return render(request,'edu/admissionstatus.html',{'admstatus':admstatus})

@csrf_exempt
def success_payment(request):
        if request.method == "POST":
          a = request.POST
          order_id = ""
          for key , val in a.items():
               if key == 'razorpay_order_id':
                    order_id = val
          user = Payment.objects.filter(paymentid = order_id).first()
          user.paid = True
          user.save()          
        return render(request,'edu/paymentsucsess.html')

def payment_print(request):
   return render(request,"edu/paymentprintreciept.html")

def feedback(request):
  if request.method=="POST":
    form = FeedbackForm(request.POST)
    if form.is_valid():
       name = form.cleaned_data['name']
       email = form.cleaned_data['email']
       message =form.cleaned_data['message']
       reg = Feedback(name=name,email=email,message=message)
       reg.save()
       messages.success(request,'Your Feedback form has been submited Successfully!') 
       form=FeedbackForm() 
    return render(request,'edu/feedback.html',{'form':form})
  else:
    form = FeedbackForm()
  return render(request,'edu/feedback.html',{'form':form})


   