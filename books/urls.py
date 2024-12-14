# books/urls.py
from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', views.book_list, name='book_list'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('genre/<int:genre_id>/', views.book_list_by_genre, name='book_list_by_genre'),
    path('author/<int:author_id>/', views.book_list_by_author, name='book_list_by_author'),
]
