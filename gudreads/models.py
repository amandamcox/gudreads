from django.db import models
from django.contrib.auth.models import User


class BookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, default='')
    book_rating = models.IntegerField(blank=True, null=True)
    book_description = models.CharField(max_length=350, blank=True, null=True)
    book_author = models.CharField(max_length=100, blank=True, null=True)
    book_image = models.URLField(max_length=300, blank=True, null=True)
    book_was_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
