from rest_framework import filters , viewsets
from rest_framework import generics, permissions
from .models import Book , Author
from .serializers import BookSerializer , AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend



#  Anyone can view the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Or your existing IsAuthenticatedOrReadOnly

    #  Add Filtering & Searching & Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

   
    filterset_fields = ['title', 'publication_year', 'author__name']

   
    search_fields = ['title', 'author__name']

    
    ordering_fields = ['title', 'publication_year']

#  Anyone can view a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


#  Only authenticated users can create a book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        #  Custom Logic Before Saving
        print(" Creating a new Book...")  
        serializer.save()  # Actual save operation


#  Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        print(" Updating a book...")  # Custom pre-processing
        return super().update(request, *args, **kwargs)


#  Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

