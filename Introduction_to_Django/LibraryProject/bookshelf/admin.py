from django.contrib import admin
from .models import Book

# Customize how the Book model appears in the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters (sidebar) for easier navigation
    list_filter = ('publication_year', 'author')

    # Add search capability
    search_fields = ('title', 'author')

