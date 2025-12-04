from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home (request):
    context = {}
    return render(request, 'AuthApp/home.html',context)
    
@login_required(login_url='login')
def profile(request):
    context = {}

    return render(request, 'AuthApp/profile.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist") 

        user = authenticate(request, username=username, password =password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            print("Username or password is incorrect")


    context = {}
    return render(request, 'AuthApp/login_form.html',context)
    
def logoutUser(request):
    context ={}
    logout(request)
    return redirect('home')
    

def register_jobseeker(request):
    context = {}
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.username = f"@{user.username}"
            user.save()

            login(request,user)
            return redirect('profile')

    context ={"form":form}
    return render(request,'authApp/register_form.html',context)


   


def register_employer(request):
     context = {}
     form = UserCreationForm()
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.username = f"@{user.username}"
            user.save()

            login(request,user)
            return redirect('profile')

     context ={"form":form}
     return render(request,'authApp/register_form.html',context)

   


