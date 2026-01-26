from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register CustomUser
@admin.register(CustomUser)
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

# Register Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
