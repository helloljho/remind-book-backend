from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'writer',
            'title',
            'author',
            'publisher',
            'review',
            'create_date',
            'modify_date',
        )
        model = Books

