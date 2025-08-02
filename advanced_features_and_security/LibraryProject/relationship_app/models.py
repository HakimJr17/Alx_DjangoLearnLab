# bookshelf/models.py  <-- CORRECTED FILE HEADER

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Custom User Manager inheriting from BaseUserManager ---
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('LIBRARIAN', 'Librarian'),
        ('MEMBER', 'Member'),
    )

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')

    objects = BaseUserManager()

    def __str__(self):
        return self.username


# --- Existing Models from your code ---

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    libraries = models.ManyToManyField('Library', related_name='books')

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change existing books"),
            ("can_delete_book", "Can delete books"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    class Meta:
        permissions = [
            ("can_manage_library", "Can manage library details (add/edit/delete)"),
        ]

    def __str__(self):
        return self.name

# --- NEW: A better way to handle librarians ---
# We use a OneToOneField to link a Library to a CustomUser
'''class LibrarianProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.user.username} at {self.library.name}"
'''

# We'll use signals to automatically create a LibrarianProfile when a user's role is set to Librarian
''' @receiver(post_save, sender=CustomUser)
def create_librarian_profile(sender, instance, created, **kwargs):
    if instance.role == 'LIBRARIAN' and not hasattr(instance, 'librarianprofile'):
        LibrarianProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_librarian_profile(sender, instance, **kwargs):
    if hasattr(instance, 'librarianprofile'):
        instance.librarianprofile.save()

# We'll need to remove the old Librarian model from your app's code if it exists.
# We will use the LibrarianProfile instead.'''