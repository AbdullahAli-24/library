from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='books_covers/', blank=True, null=True)

    def __str__(self):
        return self.title