from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, BookViewSet

# Router DRF pour les ViewSets (CRUD automatique)
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Combiner routes automatiques + route personnalisée
urlpatterns = [
    path('health/', health),           # route personnalisée
    path('', include(router.urls)),    # routes CRUD automatiques
]
