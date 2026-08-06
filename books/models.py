from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


def upload_image(instance ,file_name):
     image_name , extension=file_name.rsplit('.', 1)
     return 'books/%s.%s'%(instance.id,extension)
       

class Book(models.Model):
    title = models.CharField( max_length=200 )
    author = models.CharField( max_length=150 )
    isbn = models.CharField( max_length=20, unique=True, null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE )
    publish_date = models.DateField( null=True, blank=True )
    quantity = models.PositiveIntegerField( default=1 )
    available_quantity = models.PositiveIntegerField( default=1 )
    cover = models.ImageField( upload_to=upload_image, blank=True, null=True )
    description = models.TextField( blank=True)
    language = models.CharField( max_length=100, default="English",blank=True )
    pages = models.PositiveIntegerField( null=True, blank=True )
    created_at = models.DateTimeField( auto_now_add=True )
    @property
    def available(self):
        return self.available_quantity > 0

    @property
    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return round( sum(r.stars for r in ratings) / ratings.count(), 1)
        return 0

    @property
    def ratings_count(self):
        return self.rating_set.count()

    def __str__(self):
        return self.title
    
class Rating(models.Model):

    STARS = (
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    )
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    book = models.ForeignKey( Book, on_delete=models.CASCADE)
    stars = models.IntegerField( choices=STARS)
    created_at = models.DateTimeField(auto_now_add=True )
    class Meta:
        unique_together = ("user", "book")
    def __str__(self):
        return f"{self.user.username} rated {self.book.title}"

class Favorite(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    book = models.ForeignKey( Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True )

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} ❤️ {self.book.title}"