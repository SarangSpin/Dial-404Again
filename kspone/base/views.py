from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views import View
from .pdf import html2pdf
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
                
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password error")
    context = {}
    return render(request, 'loginpage.html', context)
def logoutuser(request):
     logout(request)
     return redirect("login")
def loginhelp(request):

        context = {}
        return render(request, 'loginhelp.html', context)

@login_required(login_url='login/login')
def home(request):
     context = {}
     return render(request, 'home.html', context)
def search(request):
      context = {}
      return render(request, 'search.html', context)
def fingerprint(request):
      context = {}
      return render(request, 'fingerprint.html', context)
def userguide(request):
      context = {}
      return render(request, 'userguide.html', context)
def pdf(request):
     pdf = html2pdf("pdf.html")
     return HttpResponse(pdf, content_type="application/pdf")
     

