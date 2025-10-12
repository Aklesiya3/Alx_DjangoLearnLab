from django.urls import path
from . import views
urlpatterns=[
    path('', views.home_view, name='home'),       # Home page at '/'
    path('about/', views.about_view, name='about'), # About page at '/about/'
    path('books/', views.book_list_view, name='book-list'), # Book list at '/books/'
]