from django.db import models

# Create your models here.



class Books(models.Model):
    Book_Name=models.CharField(max_length=200)
    Author_Name=models.CharField(max_length=200)
    isbn=models.CharField(max_length=20)
    Category=models.CharField(max_length=200)

#librarian
class Librarians(models.Model):
    Librarian_Name=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    contact_number=models.IntegerField()
    Email=models.CharField(max_length=200)

# student details
class Students(models.Model):
    Student_Name=models.CharField(max_length=200)
    Roll_Numner=models.IntegerField()
    Department=models.CharField(max_length=200)
    Contact_Number=models.IntegerField()
    unique_id=models.CharField(max_length=10,blank=True,editable=False,unique=True,)
    
#issue book details
class IssueBooks(models.Model):
    Student_Name=models.CharField(max_length=200)
    Book_Name=models.CharField(max_length=200)
    isbn=models.IntegerField()
    issue_date=models.DateField(auto_now=True)
    return_date=models.DateField()
    







