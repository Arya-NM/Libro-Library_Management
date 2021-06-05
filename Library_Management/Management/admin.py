from django.contrib import admin
from .models import Book
from .models import Librarian
from .models import students
from .models import IssueBook

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields=('Book_Name','isbn','Author_Name')  
admin.site.register(Book,BookAdmin)

class LibrarianAdmin(admin.ModelAdmin):
    search_fields=('Librarian_Name','phone_numbers','Email')
admin.site.register(Librarian,LibrarianAdmin)

class studentsAdmin(admin.ModelAdmin):
    search_fields=('Student_Name','Roll_Number','unique_id')  
admin.site.register(students,studentsAdmin)

class IssueBookAdmin(admin.ModelAdmin):
    search_fields=('Student_Name','Book_Name','isbn','issue_date','return_date')  
admin.site.register(IssueBook,IssueBookAdmin)

