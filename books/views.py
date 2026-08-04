from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book, Rating, Favorite
from .forms import BookForm


@login_required
def books(request):
    books = Book.objects.all()
    search = request.GET.get("search")
    if search:
        books = books.filter(title__icontains=search)
    favorites = Favorite.objects.filter( user=request.user).values_list( "book_id", flat=True )
    return render( request, "books/books.html", { "books": books, "favorites": favorites,})


@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    similar_books = Book.objects.filter( category=book.category).exclude( id=book.id )[:4]
    user_rating = Rating.objects.filter( user=request.user, book=book).first()
    is_favorite = Favorite.objects.filter( user=request.user, book=book).exists()
    return render( request, "books/book_detail.html",
        {
            "book": book,
            "similar_books": similar_books,
            "rating": book.average_rating,
            "ratings_count": book.ratings_count,
            "user_rating": user_rating,
            "is_favorite": is_favorite,
        }
    )



@login_required
def rate_book(request, id):
    book = get_object_or_404(Book, id=id)
    stars = int(request.POST.get("stars"))
    Rating.objects.update_or_create(user=request.user, book=book, defaults={"stars": stars})
    messages.success( request,"Thank you for rating this book." )
    return redirect( "book_detail", id=book.id)

@login_required
def toggle_favorite(request, id):
    book = get_object_or_404(Book, id=id)
    favorite = Favorite.objects.filter(user=request.user, book=book )

    if favorite.exists():
        favorite.delete()
        messages.info(request, "Removed from favorites." )
    else:
        Favorite.objects.create( user=request.user, book=book)
        messages.success( request, "Added to favorites.")
    return redirect( "book_detail", id=book.id )

@login_required
def favorite_books(request):
    favorites = Favorite.objects.filter(user=request.user )
    return render(request, "books/favorites.html",{ "favorites": favorites})


@login_required
def add_book(request):
    if not request.user.is_staff:
        return redirect("books")
    
    if request.method == "POST":
        form = BookForm( request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success( request,"Book added successfully.")
            return redirect("books")
    else:
        form = BookForm()
    return render( request,"books/book_form.html", {"form": form,"title": "Add Book"})



@login_required
def edit_book(request, id):
    if not request.user.is_staff:
        return redirect("books")
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm( request.POST, request.FILES, instance=book )
        if form.is_valid():
            form.save()
            messages.success( request, "Book updated successfully.")
            return redirect("books")
    else:
        form = BookForm(instance=book)
    return render(request,  "books/book_form.html", { "form": form,"title": "Edit Book" })


@login_required
def delete_book(request, id):
    if not request.user.is_staff:
        return redirect("books")
    
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, "Book deleted successfully." )
    return redirect("books")