from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Genre
from borrowing.models import Borrowing


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    borrowed = False
    if request.user.is_authenticated:
         borrowed = Borrowing.objects.filter(book=book, user=request.user, is_returned=False).exists()
    return render(request, 'books/book_detail.html', {'book': book, 'borrowed': borrowed})


def book_list_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/book_list.html', {'books': books, 'genre': genre})


def book_list_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(authors=author)
    return render(request, 'books/book_list.html', {'books': books, 'author': author})


def home(request):
    recommended_books = Book.objects.all()[:3]  # Пример: выбираем 3 случайные книги
    return render(request, 'books/index.html', {'recommended_books': recommended_books})

