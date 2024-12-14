from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('log_out/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit_profile', views.edit_profile_view, name='edit_profile'),
]
