from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet, 'genres')
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'book-authors', BookAuthorViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]