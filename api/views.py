from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .rabbitmq import publish_event

@api_view(['GET'])
def health(request):
    cache.set('status', 'ok', 60)
    return Response({"status": cache.get('status')})

class BookViewSet(viewsets.ModelViewSet): # Viewset = CRUD automatique
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        book = serializer.save()

        publish_event(
            'book_created', {
                'id': book.id,
                'title': book.title,
                'author_id': book.author.id
            }
        )

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer