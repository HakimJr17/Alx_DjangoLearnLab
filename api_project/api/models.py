from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    '''
    The purpose of this method is to ensure the Author class is represented in a well 
    human-readable string representation of an object as opposed to the less descriptive
    name <Author: Author object (1)>..
    '''

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title
    

    '''
    The on_delete=models.CASCADE means that if an Author is deleted, 
    all of their associated Book records will also be automatically deleted.
    The instructions on ALX had initially stated that we just define tha author attribute inside 
    the book class but the reasoning for differentiating them is that this approach enhances 
    flexibility and scalability should if we wnated to add more attributes to our Author class
    '''