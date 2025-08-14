from django.urls import path
from .views import BookList


urlpatterns = [path('books/', BookList.as_view(), name='book-list'),] # Maps to the BookList view

'''
The path function in url_patterns variable takes in two variables.
The first variable is the route and the second is the view
'''