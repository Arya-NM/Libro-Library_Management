from django.shortcuts import render
from django.db import models

# Create your views here.


def home(request):
	return render( request, 'index.html')

def signup(request):
	return render(request,'sign_up.html')

def contact(request):
	return render(request,'contactus.html')



