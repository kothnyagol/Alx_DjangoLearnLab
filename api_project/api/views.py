from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions

# Existing list-only view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New CRUD view using ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
