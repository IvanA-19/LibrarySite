# books/models.py
from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    biography = models.TextField(blank=True, verbose_name='Биография')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название издательства')
    address = models.TextField(blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='URL')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    isbn = models.CharField(max_length=20, unique=True, verbose_name='ISBN')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Издательство')
    publication_date = models.DateField(blank=True, null=True, verbose_name='Дата публикации')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Обложка')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

