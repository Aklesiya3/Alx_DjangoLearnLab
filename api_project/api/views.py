from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated] 
