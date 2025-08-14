from rest_framework import serializers
#the line imports the entire DRF serializers library. 

from .models import Book

# ModelSerializer is a class that exists within the serializers library.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


'''
class Meta has to be included because it provides the essential instructions that the 
serializer needs to function. Without this line, the serializer has no idea which 
database table to look at.
fields = '__all__': This tells the serializer which fields from the Book model 
should be included in the API's output. 
'''