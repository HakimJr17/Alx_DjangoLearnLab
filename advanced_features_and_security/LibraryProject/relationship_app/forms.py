# relationship_app/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Add a field for the role, which is one of our custom fields
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, initial='MEMBER')

    class Meta(UserCreationForm.Meta):
        # Tell the form to use our CustomUser model
        model = CustomUser
        # Tell the form which fields to display
        # We include all the standard fields plus our new 'role' field
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'role')