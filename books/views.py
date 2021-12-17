from django.shortcuts import render
from rest_framework import generics

from .models import Books
from .serializers import BooksSerializer


# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
