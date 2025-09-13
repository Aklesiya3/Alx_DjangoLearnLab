# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views you created

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
