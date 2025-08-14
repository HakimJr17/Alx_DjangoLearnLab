from rest_framework import serializers
#the line imports the entire DRF serializers library. 

from .models import Book, Author

# ModelSerializer is a class that exists within the serializers library.
class BookSerializer(serializers.ModelSerializer):
    #author = serializers.StringRelatedField(read_only=True)
# By adding this line, unlike in the previous version, 
# it tells the serializer to display a more descriptive field, like the author's name
# StringRelatedField, which will automatically use the __str__ method of the related model 
# (the Author model in this case).
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
# We have changed from a StringRelatedField to PrimaryKeyRelatedField becuase --->
# we need to get a working form for creating new books, 
# and that means changing your author field in the BookSerializer to a writable field. 
# The most common one for a foreign key relationship is serializers.PrimaryKeyRelatedField. 
# This will display a dropdown menu of all the existing authors in your database, 
# allowing you to select one.
    class Meta:
        model = Book
        fields = ['author', 'title']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

'''
class Meta has to be included because it provides the essential instructions that the 
serializer needs to function. Without this line, the serializer has no idea which 
database table to look at.
fields = '__all__': This tells the serializer which fields from the Book model 
should be included in the API's output. 
'''

'''
Initially, I had the BookSerializer class written in the folloing format and it was not ideal
becuase the author's primary key (being the foreign key in the Book class) was being 
shown in the API and that's not ideal. The format for the BookSerializer class was as follows:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
'''