from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books" ),
    path( "details/<int:id>/", views.book_detail, name="book_detail" ),
    path( "rate/<int:id>/", views.rate_book, name="rate_book" ),
    path( "favorite/<int:id>/", views.toggle_favorite, name="toggle_favorite"),
    path( "favorites/", views.favorite_books, name="favorite_books" ),
    path( "add/", views.add_book, name="add_book"),
    path( "edit/<int:id>/",views.edit_book, name="edit_book"),
    path( "delete/<int:id>/", views.delete_book, name="delete_book"),
]