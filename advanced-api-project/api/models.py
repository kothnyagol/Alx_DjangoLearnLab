from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """Represents an author who can have multiple books."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book with a title, publication year, and linked author."""
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def clean(self):
        """Ensure publication_year is not in the future."""
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
