from django.template.defaulttags import url
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from setuptools.extern import names

from .import views
# from .WebBooks.urls import urlpatterns

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
    re_path(r'^book/create/$', views.BookCreate.as_view(),
        name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(),
        name='book_update'),
    re_path(r'book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(),
        name='book_delete'),
]