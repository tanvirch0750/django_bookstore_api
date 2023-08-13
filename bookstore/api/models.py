from django.db import models


# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-fi', 'Sci-fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
        ('Fantay', 'Fantasy')
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORY)
    book_cover = models.CharField(max_length=500)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
