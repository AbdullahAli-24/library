from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from books.models import Book
from .models import Loan

@login_required
def borrow_book(request, id):
    book = get_object_or_404( Book, id=id)
    if book.available_quantity <= 0:
        messages.error( request,"This book is not available.")
        return redirect("books")

    already = Loan.objects.filter( user=request.user, book=book, returned=False ).exists()
    if already:
        messages.warning( request,"You already borrowed this book." )
        return redirect("books")

    Loan.objects.create( user=request.user, book=book)
    book.available_quantity -= 1
    book.save()
    messages.success( request, "Book borrowed successfully." )
    return redirect("books")

@login_required
def return_book(request, id):
    loan = get_object_or_404( Loan, id=id,user=request.user,returned=False)
    loan.returned = True
    loan.returned_at = timezone.now()
    loan.save()

    loan.book.available_quantity += 1
    loan.book.save()
    messages.success( request, "Book returned successfully." )
    return redirect("my_loans")

@login_required
def my_loans(request):
    loans = Loan.objects.filter( user=request.user ).select_related( "book" ).order_by( "-borrowed_at" )
    return render( request, "loan/my_loans.html",{ "loans": loans })

    