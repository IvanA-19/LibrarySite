# books/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Book, Author, Genre, Publisher


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'quantity', 'cover_image_display')
    list_filter = ('publisher', 'genre')
    search_fields = ('title', 'authors__first_name', 'authors__last_name', 'publisher__name', 'isbn')
    filter_horizontal = ('authors', 'genre')
    fields = ('title', 'slug', 'authors', 'isbn', 'publisher', 'publication_date', 'description', 'cover_image', 'genre', 'quantity')  # Добавляем fields для удобного редактирования
    readonly_fields = ('cover_image_display',)  # Помечаем поле как только для чтения
    prepopulated_fields = {'slug': ('title',)} # Добавляем автоматическое заполнение

    def cover_image_display(self, obj):
        """Отображает миниатюру обложки в списке книг."""
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.cover_image.url
            )
        return "Нет обложки"

    cover_image_display.short_description = 'Обложка'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)