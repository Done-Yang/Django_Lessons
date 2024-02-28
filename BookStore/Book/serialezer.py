from rest_framework import routers, serializers, viewsets
from .models import Book
from .serialezer import BookSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['code', 'name', 'description', 'price']
