from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('create_book/', createBook, name='createbook'),
    path('updatebook/<str:pk>/', updateBook, name='updatebook'),
    path('deletebook/<str:pk>/', deleteBook, name='deletebook'),
    path('create_menu/', createMenu, name='createmenu'),
    path('updatemenu/<str:pk>/', updateMenu, name='updatemenu'),
    path('deletemenu/<str:pk>/', deleteMenu, name='deletemenu'),
    path('updatecontact/<str:pk>/', updateContact, name='updatecontact'),
    path('deletecontact/<str:pk>/', deleteContact, name='deletecontact'),
]
