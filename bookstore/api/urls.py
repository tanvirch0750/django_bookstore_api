from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookListView, basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('books/', views.BookListView.as_view()), #handle get and post request
    # path('books/<int:pk>/', views.BookListUpdateDelete.as_view()), #handle single get, update and delete request
    path('', include(router.urls))
]