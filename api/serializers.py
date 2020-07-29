from rest_framework import serializers
from .models import Book, Note, status_choices
from .models import User



class NestedNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['body']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    notes = NestedNoteSerializer(many=True, required= False)
    
    class Meta: 
        model = Book
        fields = ['url', 'id', 'title', 'author',  'status', 'added_on', 'notes']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['url', 'id', 'page_number', 'body', 'book', 'owner', 'created_on']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only = True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'books']