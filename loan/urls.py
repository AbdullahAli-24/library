from django.urls import path
from . import views

urlpatterns = [
    path( "", views.my_loans, name="my_loans"),
    path( "borrow/<int:id>/", views.borrow_book, name="borrow_book" ),
    path( "return/<int:id>/", views.return_book, name="return_book" ),
]