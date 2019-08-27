from django.urls import path
from .views import list_mangas, create_manga,update_manga,delete_manga

urlpatterns = [
    path('', list_mangas, name='list_mangas'),
    path('new', create_manga, name='create_manga'),
    path('update/<int:id>/', update_manga, name='update_manga'),
    path('delete/<int:id>/', delete_manga, name='delete_manga'),
]
