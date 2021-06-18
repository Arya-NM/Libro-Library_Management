
#from django import forms
from django.db.models import query
from .models import Book, IssueBook, students
from django.http import request, response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
import random,os


# Create your views here.



def ref():
	unique_id=int(random.randint(111,999))
	return unique_id

def home(request):
	return render( request, 'index.html')


def homepg(request):
	return render(request, 'homepage.html')


def contact(request):
	return render(request,'contactus.html')

#def addbooks(request):
	#return render(request,'addbook.html')

def addbooks(request):
	responseDic = {}
	try:
		Book_Name = request.POST['Book_Name']
		Author_Name = request.POST['Author_Name']
		ISBN = request.POST['isbn']
		Status = request.POST['Status']
		Category = request.POST['Category']

		booklist = Book(Book_Name=Book_Name,Author_Name=Author_Name,isbn=ISBN,Status=Status,Category=Category)
		booklist.save()
		responseDic["msg1"]="book Added"
		return render(request, "homepage.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="book cannot be Added"
		 return render(request, "addbook.html", responseDic)



#def viewbooks(request):
	#return render(request,'viewbook.html')

def viewbooks(request):
	books=Book.objects.all()
	return render(request,"viewbook.html",{'books':books})


def delete_data(request,id):
	if request.method =='POST':
		pi=Book.objects.get(pk=id)
		pi.delete()
		return render(request,"homepage.html")

def update_data(request,pk):
	prod=Book.objects.get(id=pk)
	if request.method=="POST":
		#if len(request.FILES)!=0:
			#if len(prod.imgs)>0:
				#os.remove(prod.imgs.path)
			#prod.imgs=request.FILES['imgs']
		prod.Book_Name=request.POST['Book_Name']
		prod.Author_Name=request.POST['Author_Name']
		prod.isbn=request.POST['isbn']
		prod.Status=request.POST['Status']
		prod.Category=request.POST['Category']
		prod.save()
		return render(request,"homepage.html")		
	context={'prod':prod}
	return render(request,"editbook.html",context)


def issuebooks(request):
	responseDic = {}
	try:
		Student_Name = request.POST['Student_Name']
		Book_Name = request.POST['Book_Name']
		ISBN = request.POST['isbn']
		issue_date = request.POST['issue_date']
		return_date = request.POST['return_date']

		bookslist =  IssueBook(Student_Name=Student_Name,Book_Name=Book_Name,isbn=ISBN,issue_date=issue_date,return_date=return_date)
		bookslist.save()
		responseDic["msg1"]="issue book Added"
		return render(request, "homepage.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="issue book cannot be Added"
		 return render(request, "issuebook.html", responseDic)
	


def viewissuebooks(request):
	issuebooks=IssueBook.objects.all()
	return render(request,"viewissuebook.html",{'issuebooks':issuebooks})


def deleteissue_data(request,id):
	if request.method =='POST':
		pi=IssueBook.objects.get(pk=id)
		pi.delete()
		return render(request,"homepage.html")


def updateissue_data(request,pk):
	prod=IssueBook.objects.get(id=pk)
	if request.method=="POST":
		#if len(request.FILES)!=0:
			#if len(prod.imgs)>0:
				#os.remove(prod.imgs.path)
			#prod.imgs=request.FILES['imgs']
		prod.Student_Name=request.POST['Student_Name']
		prod.Book_Name=request.POST['Book_Name']
		prod.isbn=request.POST['isbn']
		prod.issue_date=request.POST['issue_date']
		prod.return_date=request.POST['return_date']
		prod.save()
		return render(request,"homepage.html")		
	context={'prod':prod}
	return render(request,"editissuebook.html",context)



def addstudents(request):

	responseDic = {}
	try:
		Book_Name = request.POST['Book_Name']
		Author_Name = request.POST['Author_Name']
		ISBN = request.POST['isbn']
		Status = request.POST['Status']
		Category = request.POST['Category']

		booklist = Book(Book_Name=Book_Name,Author_Name=Author_Name,isbn=ISBN,Status=Status,Category=Category)
		booklist.save()
		responseDic["msg1"]="book Added"
		return render(request, "homepage.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="book cannot be Added"
		 return render(request, "addbook.html", responseDic)
	#return render(request,'addstudent.html')

def viewstudents(request):
	return render(request,'viewstudent.html')

#def editbooks(request):
	#return render(request,'editbook.html')


def details(request):
	return render(request,'adddetails.html')


def stuhomepg(request):
	return render(request,'stuhomepage.html')

def stuviewissuebooks(request):
	return render(request,'stuviewissuebook.html')

def fan1learnmores(request):
	return render(request,'fan1learnmore.html')

def fantwolearnmores(request):
	return render(request,'fantwolearnmore.html')

def fanthreelearns(request):
	return render(request,'fanthreelearn.html')

def fanfoures(request):
	return render(request,'fanfoure.html')

def eduones(request):
	return render(request,'eduone.html')

def edutwos(request):
	return render(request,'edutwo.html')

def eduthrees(request):
	return render(request,'eduthree.html')

def edufours(request):
	return render(request,'edufour.html')

def bioones(request):
	return render(request,'bioone.html')

def biotwos(request):
	return render(request,'biotwo.html')

def biothrees(request):
	return render(request,'biothree.html')

def biofours(request):
	return render(request,'biofour.html')




def edu_ref(request):
	edubooks=IssueBook.objects.all()
	return render(request,"edu&ref.html",{'edubooks':edubooks})
	


def stu_login(request):
	responseDic={}
	email = request.POST.get('email')
	password = request.POST.get('password')
	user = authenticate(request,email=email,password=password)
	print(email,password)
	if user is not None:
		login(request,user)
		print("user")
		return redirect('stulogin.html')
	else:
		return render(request,'Registration/stulogin.html')



def stu_signup(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		username=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('psw')
		repeat_password=request.POST.get('psw-repeat')
		user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
		user.save()
		print("User Created")
		return redirect('/')
	else:
		return render(request,'Registration/stusignup.html')





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


#librarian login

def login_view(request):
	responseDic={}
	user_name = request.POST['username']
	password = request.POST['password']
	user = authenticate(request,username=user_name,password=password)
	print("user")
	if user is not None:
		login(request,user)
		return render(request,'/')
	else:
		return redirect(request,'login.html')


def logout_view(request):
	logout(request)
	return redirect('login')




	








