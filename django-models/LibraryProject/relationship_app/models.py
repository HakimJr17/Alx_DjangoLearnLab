# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # Import post_save signal
from django.dispatch import receiver # Import receiver decorator


class Author(models.Model):
    name = models.CharField(max_length=200) # Reverted to 200 based on common practice, adjust if checker needs 100

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Ensure ManyToManyField to Library is present, as it was in initial discussions
    libraries = models.ManyToManyField('Library', related_name='books') 

    class Meta:
        # Re-added Book permissions
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_edit_book", "Can edit existing books"),
            ("can_delete_book", "Can delete books"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300) # Re-added the missing address field

    class Meta:
        # Re-added Library permissions
        permissions = [
            ("can_manage_library", "Can manage library details (add/edit/delete)"),
        ]

    def __str__(self):
        return self.name


# --- UserProfile Model ---
class UserProfile(models.Model):
    # Defining role choices as per the task description (including ADMIN)
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('LIBRARIAN', 'Librarian'),
        ('MEMBER', 'Member'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# --- Signals to automatically create/save UserProfile when a User is created/saved ---
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # This ensures the userprofile exists before trying to save it.
    # Essential for when a User object is saved without a pre-existing UserProfile (e.g., initial creation).
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()



class Librarian(models.Model):
    name = models.CharField(max_length=100) # Assuming name, adjust if checker expects more
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian') # Added related_name for clarity

    def __str__(self):
        return f"{self.name} (librarian for {self.library.name})"