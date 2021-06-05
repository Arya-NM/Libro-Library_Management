from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
import random

# Create your views here.


def home(request):
	return render( request, 'index.html')


def login(request):
	return render(request,'Registration/login.html')

def contact(request):
	return render(request,'contactus.html')



#sign up
def signup(request):
	if request.method=="POST":
		user_name=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('psw')
		repeat_password=request.POST.get('psw-repeat')
		user=User.objects.create_user(username=user_name,email=email,password=password)
		user.save()
		print("User Created")
		return redirect('login')
	else:
		return render(request,'Registration/sign_up.html')



