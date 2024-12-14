# borrowing/urls.py
from django.urls import path
from . import views


app_name = 'borrow'

urlpatterns = [
    path('borrow/<slug:book_slug>/', views.borrow_book, name='borrow_book'),
    path('return/<int:borrowing_id>/', views.return_book, name='return_book'),
]
