from django.shortcuts import render,redirect
from .forms import UserSignupForm,UserLoginForm
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def UserSignupView (request):
    if request.method == 'POST':
        form=UserSignupForm(request.POST or None )
        if form .is_valid():
           email= form.cleaned_data['email']
           form. save()
           send_mail(
              subject='Welcome to bug tracking system',
              message= 'Thank you for singup to our bug tracking system We are glad to have you on borad',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email],
           )
           return redirect("login")
        else :
           return render(request,'core/singup.html',{'form':form})
    else :
        form = UserSignupForm()
        return render(request,'core/singup.html',{'form':form})
    
def userLoginView(request):
  if request.method =="POST":
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
      print(form.cleaned_data)
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(request,email=email,password=password) #it will check in database..
      if user:
        login(request,user)
        if user.role == "Project Manager":
          return redirect("Project_Manager") #parking.urls.py name...
        elif user.role == "Developer":
          return redirect("Developer_dashbord") #parking.urls.py name...
        else:
           if user.role == "Tester":
              return redirect("Tester_dashbord")
           else:
              if user.role == "admin":
                 return redirect("Admin_deashbord")
      else:

        return render(request,'core/login.html',{'form':form})  
    
  else:
    form = UserLoginForm()
    return render(request,'core/login.html',{'form':form})