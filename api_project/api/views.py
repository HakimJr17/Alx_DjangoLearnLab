from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
#class BookList(generics.ListAPIView):
# queryset = Book.objects.all()
# serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

'''
In this context, the BookViewSet inherits from the ModelViewSet class provided by DRF. 
This class automatically provides the following actions:

list: Retrieve a list of model instances.
create: Create a new model instance.
retrieve: Retrieve a single model instance.
update: Update a model instance.
partial_update: Update a model instance with a partial set of fields.
destroy: Delete a model instance.
'''