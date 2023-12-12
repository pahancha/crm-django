from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

from .forms import SignUpForm, AddCustomerRecordForm

# Create your views here.
def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
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
        return render(request,'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
                  
			# User authentication
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})      


def customer_record(request, pk):
      if request.user.is_authenticated:
            customer_reco = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_reco})
      else:
            messages.success(request, "You must have the necessary authorization to access these records.")
            return redirect('home')
      

def delete_customer_record(request, pk):
      if request.user.is_authenticated:
            
        delete = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request, "Customer record deleted successfully.")
        return redirect('home')
      
      else:
           messages.error(request, "You must have the necessary authorization to access these records.")
           return redirect('home')
           
def add_customer_record(request):
     form = AddCustomerRecordForm(request.POST or None)
     if request.user.is_authenticated:
          if request.method == "POST":
               if form.is_valid():
                    add_record = form.save()
                    messages.success(request, "Customer record has beed added.")
                    return redirect('home')
               
          return render(request, 'add_record.html', {'form': form})
     else:
          messages.error(request, "You must have the necessary authorization to access these records.")
          return redirect('home')
     

def update_customer_record(request, pk):
     if request.user.is_authenticated:
          current_record = Record.objects.get(id=pk)
          form = AddCustomerRecordForm(request.POST or None, instance=current_record)

          if form.is_valid():
               form.save()
               messages.success(request, "Customer record has been updated!")
               return redirect('home')
          return render(request, 'update_record.html', {'form': form})
     else:
               messages.error(request, "You must have the necessary authorization to access these records.")
               return redirect('home')
          
          


                           
      