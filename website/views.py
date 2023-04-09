from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records= Record.objects.all()

    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged In !")
            return redirect('home')
        else:
            messages.success(request,'There was an error logging In , Please Try Again ...')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

#def login_user(request):
   # pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out ...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have succesfully  Register")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You Must be Logged In To view That Page.")
        return redirect('home')