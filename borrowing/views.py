# borrowing/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Borrowing
from books.models import Book


@login_required
def borrow_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    borrowed = Borrowing.objects.filter(book=book, user=request.user, is_returned=False).exists()

    if borrowed:
        messages.error(request, f'Вы уже забронировали книгу "{book.title}".')
        return redirect('books:book_detail', slug=book_slug)

    if book.quantity > 0:
        Borrowing.objects.create(book=book, user=request.user)
        book.quantity -= 1
        book.save()
        messages.success(request, f'Вы успешно забронировали книгу "{book.title}".')
        return redirect('books:book_detail', slug=book_slug)
    else:
        messages.error(request, 'Книга не доступна для бронирования, так как закончилась на складе.')
        return redirect('books:book_detail', slug=book_slug)


@login_required
def return_book(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, pk=borrowing_id, user=request.user, is_returned=False)
    book = borrowing.book
    borrowing.is_returned = True
    book.quantity += 1
    book.save()
    borrowing.save()
    messages.success(request, f'Вы успешно вернули книгу "{book.title}".')
    return redirect('books:home')
