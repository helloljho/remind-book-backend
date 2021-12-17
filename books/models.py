from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer_book')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    review = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Highlight(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer_Highlight')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    contents = models.TextField()
    memo = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()

