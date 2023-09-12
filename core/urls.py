from django.urls import path
from . import views

urlpatterns = [
    # главная страница
    path('', views.frontpage, name='frontpage'),
    # регистрация пользователя
    path('signup/', views.signup, name='signup'),
    # вход пользователя
    path('login/', views.login, name='login'),
    # выход пользователя
    path('user-logout/', views.logout, name='logout'),
    # CRUD
    
    # страница пользователя
    path('dashboard/', views.dashboard, name='dashboard'),
    # создать запись пользователя
    path('create-record/', views.create_record, name='create-record'),
    # обновить запись пользователя
    path('update-record/<int:pk>/', views.update_record, name='update-record'),
    # обзор запись пользователя
    path('record/<int:pk>/', views.singular_record, name='record'),
    # удалить запись пользователя
    path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),
]
