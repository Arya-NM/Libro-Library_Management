from django.db import models
from django.core.validators import RegexValidator



# Create your models here.


class Book(models.Model):
    Book_Name=models.CharField(max_length=200)
    Author_Name=models.CharField(max_length=200)
    isbn=models.CharField(max_length=20)
    Status=models.CharField(max_length=20)
    Category=models.CharField(max_length=200)

    def __str__(self):
        return self.Book_Name


#librarian
class Librarian(models.Model):
    Librarian_Name=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Email=models.CharField(max_length=200)

    def __str__(self):
        return self.Librarian_Name


# student details
class students(models.Model):
    Student_Name=models.CharField(max_length=200)
    Roll_Number=models.IntegerField()
    Department=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    unique_id=models.CharField(max_length=10,blank=True,editable=False,unique=True,)
    
    #models.CharField(max_length=10,blank=True,editable=False,unique=True,)
    def __str__(self):
        return self.unique_id
    
#issue book details
class IssueBook(models.Model):
    Student_Name=models.CharField(max_length=200)
    Book_Name=models.CharField(max_length=200)
    isbn=models.IntegerField()
    issue_date=models.DateField(blank=True, default='', null=True)
    return_date=models.DateField(blank=True, default='', null=True)

    def __str__(self):
        return self.Student_Name






