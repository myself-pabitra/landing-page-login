from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
# from DjangoTemplate.myapp.models import Contact


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        obj = Contact(name = name, email = email , message = message)
        obj.save()
        messages.success(request,'Thank you for contacting us.. we have received your message . we will respond to you within 48 hours.')



    return render(request, 'contact.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'login Successful ! welcome')
            return redirect('home')
        else:
            messages.error(request,'Please enter valid login password or username !')
            return redirect(login_user)
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'This Username already Exists..!!')
                return redirect(register_user)
            elif User.objects.filter(email =email).exists():
                messages.error(request, 'This email already Exists..!!')
                return redirect(register_user)
            else:
                user = User.objects.create_user(username = username , password= password ,email = email)
                user.save()
                messages.success(request, 'User created Successfully..')
            return redirect('login')
        else:
            messages.info(request, 'Password Does not match')
            return redirect(register_user)

    return render(request,'register.html')

def logout_user(request):
    logout(request)
    return redirect(login_user)
