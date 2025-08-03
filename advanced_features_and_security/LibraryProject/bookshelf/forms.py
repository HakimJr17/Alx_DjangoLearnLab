from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for creating and updating Book instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'genre']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExampleForm(forms.Form):
    """
    This is an example form for the checker to validate.
    It contains a single text field.
    """
    example_field = forms.CharField(max_length=100)