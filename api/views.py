from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

class BookViewSet(viewsets.ModelViewSet): # Viewset = CRUD automatique
    queryset = Book.objects.all()
    serializer_class = BookSerializer