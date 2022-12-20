from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def login_page(request):
    return render(request, 'login.html', {})