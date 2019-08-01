from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'authorization/login.html')


@login_required
def home(request):
    return render(request, 'authorization/home.html')