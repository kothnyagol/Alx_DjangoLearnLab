from .models import Book
from django.contrib import admin
from accounts.models import CustomUser
from accounts.admin import CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')  # Add search box for title & author
    list_filter = ('publication_year',)  # Filter by publication year
admin.site.register(Book, BookAdmin)
