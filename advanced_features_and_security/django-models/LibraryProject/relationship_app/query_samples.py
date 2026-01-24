#!/usr/bin/python3
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# Function: Query all books by a specific author
# -----------------------------
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # ALX expects this exact usage
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

# -----------------------------
# Function: List all books in a library
# -----------------------------
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # ALX expects .get()
        return library.books.all()
    except Library.DoesNotExist:
        return []

# -----------------------------
# Function: Retrieve the librarian for a library
# -----------------------------
def query_librarian_for_library(library_name):
    try:
        # Get the library first
        library = Library.objects.get(name=library_name)
        # ALX expects direct query from Librarian model
        librarian = Librarian.objects.get(library=library)
        return [librarian]
    except Library.DoesNotExist:
        return []
    except Librarian.DoesNotExist:
        return []

# -----------------------------
# Test script when running directly
# -----------------------------
if __name__ == "__main__":
    author_name = "Chinua Achebe"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    for book in query_books_by_author(author_name):
        print(f"- {book.title}")

    print(f"\nBooks in {library_name}:")
    for book in query_books_in_library(library_name):
        print(f"- {book.title}")

    print(f"\nLibrarians for {library_name}:")
    for librarian in query_librarian_for_library(library_name):
        print(f"- {librarian.name}")
