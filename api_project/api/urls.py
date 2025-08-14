#from django.urls import path, include
#from .views import BookList
from .views import BookViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'books_all')
router.register(r'authors_all', AuthorViewSet, basename = 'authors_all')

urlpatterns = router.urls

'''urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]

#urlpatterns = [path('books/', BookList.as_view(), name='book-list'),] # Maps to the BookList view


The path function in url_patterns variable takes in two variables.
The first variable is the route and the second is the view
The string 'books_all/' is not retrieved from anywhere; 
it's a static string literal that you, as the developer, define. 
It is the URL endpoint you are creating.
'''