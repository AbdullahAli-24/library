from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Loan(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE,related_name="loans")
    book = models.ForeignKey( Book, on_delete=models.CASCADE, related_name="loans")
    borrowed_at = models.DateTimeField( auto_now_add=True )
    returned = models.BooleanField( default=False )
    returned_at = models.DateTimeField( null=True, blank=True)
    class Meta:
        ordering = ["-borrowed_at"]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"