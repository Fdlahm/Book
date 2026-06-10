from django.urls import path
from .views import *
urlpatterns = [
    path('',book_list.as_view(),name="list"),
    path('book',book_create.as_view(),name="create"),
    path('book/<int:pk>',book_detail.as_view(),name="detail"),
    path('book/edit/<int:pk>',book_update.as_view(),name="edit"),
    path('book/delete/<int:pk>',book_delete.as_view(),name="delete")
]
