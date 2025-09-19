from rest_framework import generics , viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookSerializers


class BookList(generics.ListAPIview):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookViewSet(viewsets.Modelviewset):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated] 