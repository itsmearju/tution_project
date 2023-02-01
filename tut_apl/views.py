from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth

# Create your views here.

def loginPage(request):
    return render(request, 'login.html')

def tlogin(request):
    if request.method == 'POST':
        email= request.POST['email']      
        password = request.POST['password'] 
       
        user = auth.authenticate(email=email, password=password)   
        if user is not None:   
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')                #login when user variable has correct values
            else:
                login(request,user)
                auth.login(request,user) 
                return redirect('/') 

             
        else:
             return redirect('/') 
    else:
        return render('login.html')