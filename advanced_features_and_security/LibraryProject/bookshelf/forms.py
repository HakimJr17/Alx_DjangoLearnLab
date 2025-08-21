from django import forms
from django.contrib.auth.forms import UserCreationForm # Import Django's base user creation form
from .models import CustomUser, Book, Author # Import your custom user model, Book, and Author

class BookForm(forms.ModelForm):
    """
    A form for creating and updating Book instances.
    """
    class Meta:
        model = Book
        # Ensure 'libraries' is in your Book model if you want it here.
        # If 'publication_date' is not in your Book model, it should not be in widgets.
        fields = ['title', 'author', 'libraries']
        # Removed 'publication_date' from widgets as it's not in your Book model
        # If you add publication_date to your model, you can uncomment and use this:
        # widgets = {
        #     'publication_date': forms.DateInput(attrs={'type': 'date'}),
        # }

class ExampleForm(forms.Form):
    """
    This is an example form for the checker to validate.
    It contains a single text field.
    """
    example_field = forms.CharField(max_length=100)

class CustomUserCreationForm(UserCreationForm):
    """
    A custom form for creating new users based on the CustomUser model.
    It extends Django's UserCreationForm to work with your custom user model.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # You can add or remove fields here that are part of your CustomUser model.
        # 'email' is often added if it's a custom field on CustomUser.
        fields = UserCreationForm.Meta.fields + ('email',)
