from django.contrib import admin
from django.urls import path, include, re_path
from catalog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('edit1/<int:id>', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(),
            name='book-detail'),
    re_path(r'^authors/(?P<pk>\d+)?$', views.AuthorListView.as_view(),
            name='authors'),
    # Tizimga kirish uchun URL-manzillarni qo`shish
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('catalog/', include('catalog.urls')),
]
