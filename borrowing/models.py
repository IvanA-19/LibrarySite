# borrowing/models.py
from django.db import models
from django.conf import settings
from books.models import Book


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    borrow_date = models.DateField(auto_now_add=True, verbose_name='Дата бронирования')
    return_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')
    is_returned = models.BooleanField(default=False, verbose_name='Возвращено')

    def __str__(self):
        return f"Бронирование {self.book.title} пользователем {self.user.username}"

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'