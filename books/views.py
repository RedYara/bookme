from django.shortcuts import render
from .models import Books

# Create your views here.
def books(request):
    booklist = Books.objects.all()
    return render(request,"books/books.html", {"booklist":booklist})

def details(request, pk:int):
    book = Books.objects.get(pk=pk)
    return render(request,"books/details.html", {"book":book})
