from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.

# @login_required(login_url='login')
def home(request):
    return render(request, "pages/home.html", context={}, status=200)

def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
            # To do error handling...

    context =  {}
    return render(request, 'pages/login.html', context)

def register(request): 
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        # To do error handling...
    
    context =  {'form': form}
    return render(request, 'pages/register.html', context)

def problem_list(request):
    """
    ...Display all problems in a table
    """
    return
    