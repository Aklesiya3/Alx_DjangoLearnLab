from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  
]
