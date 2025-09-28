
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

#  Anyone can view the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Or your existing IsAuthenticatedOrReadOnly

    # ✅ Add Filtering & Searching & Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Step 1: Filtering (Exact Matches)
    # Example: /books/?title=Harry%20Potter
    filterset_fields = ['title', 'publication_year', 'author__name']

    # ✅ Step 2: Searching (Partial Matches, Case-Insensitive)
    # Example: /books/?search=harry
    search_fields = ['title', 'author__name']

    # ✅ Step 3: Ordering
    # Example: /books/?ordering=publication_year  or /books/?ordering=-title
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
        # ✅ Custom Logic Before Saving
        print("📌 Creating a new Book...")  
        serializer.save()  # Actual save operation


#  Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        print("✏️ Updating a book...")  # Custom pre-processing
        return super().update(request, *args, **kwargs)


#  Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


