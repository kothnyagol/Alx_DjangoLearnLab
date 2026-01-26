from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'date_of_birth')

# Register CustomUser explicitly (ALX wants this exact line)
admin.site.register(CustomUser, CustomUserAdmin)

# Book model admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
