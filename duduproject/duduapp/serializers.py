from .models import Book , Autor
from rest_framework import serializers

class Bookserializers(serializers.Modelserializer):
    model=Book
    fields='_all_'
class Autorserializers(serializers.Modelserializer):
    model=Autor
    fields='_all_'