from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate , logout

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'login Successful..!')
            return redirect('home')
        else:
            return redirect(login_user)
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect(login_user)