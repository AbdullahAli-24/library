from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'quantity',
        'available_quantity'
    )
    search_fields = (
        'title',
        'author',
        'isbn'
    )

    list_filter = ( 'category',)