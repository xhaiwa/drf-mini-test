from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

@api_view(['GET'])
def health(request):
    cache.set('status', 'ok', 60)
    return Response({"status": cache.get('status')})

class BookViewSet(viewsets.ModelViewSet): # Viewset = CRUD automatique
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # cache de la liste
    @method_decorator(cache_page(60), name='book_list')

    # cache GET :id
    @method_decorator(cache_page(60 * 2), name='book_retrieve')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @method_decorator(cache_page(60), name='author_list')
    @method_decorator(cache_page(60 * 2), name='author_retrieve')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)