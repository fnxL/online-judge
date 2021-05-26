from judge.models import Problems
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.
 

# @login_required(login_url='login')
def home(request):
    last5 = Problems.objects.all().order_by('-id')[:6]
    diff = {'1': '<span class="badge bg-success">Easy</span>',
            '2': '<span class="badge bg-warningl">Medium</span>',
            '3': '<span class="badge bg-danger">Hard</span>'
    }
    return render(request, "pages/home.html", {'last5': last5, 'df': diff}, status=200)

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
            messages.success(request,"ok")
            return redirect('login')

        # To do error handling...
    
    context =  {'form': form}
    return render(request, 'pages/register.html', context)

def problem_list(request):
    """
    ...Display all problems in a table
    """

    data = Problems.objects.all()

    
    return render(request, 'pages/problems.html', {'problems': data})
    