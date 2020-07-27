from rest_framework import serializers
from .models import Book, Note, status_choices
from .models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'status', 'added_on']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'body', 'owner', 'created_on']