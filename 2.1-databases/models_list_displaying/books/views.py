from django.shortcuts import render
from datetime import datetime
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books = Book.objects.filter(pub_date=pub_date)
    try:
        prev = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first().pub_date
    except:
        prev = None
    try:
        next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first().pub_date
    except:
        next = None
    context = {'books': books, 'prev': prev, 'next': next, 'pub_date': pub_date}
    return render(request, template, context)
