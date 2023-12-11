from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        #Authentication
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in to the CRM!")
            return redirect('home')
        else:
            messages.error(request, "There was an error loggin in. Try again.")
            return redirect('home')       
    else:
        return render(request,'home.html', {})



                