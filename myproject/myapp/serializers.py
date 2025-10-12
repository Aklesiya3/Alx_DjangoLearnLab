from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def get_days_since_created(self, obj):
        return (date.today() - obj.created_at).days