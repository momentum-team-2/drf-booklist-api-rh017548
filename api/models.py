from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Q
from django.contrib.postgres.search import SearchVector



status_choices = (
    ("to read", "to read"),
    ("reading", "reading"),
    ("read", "read"),)


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='books')
    status = models.CharField(max_length=10,
                  choices=status_choices,
                  default= 1)


class Note(models.Model):
    page_number = models.PositiveIntegerField(blank = True, null = True)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']


def get_book(queryset, user):
    if user.is_authenticated:
        books = queryset.filter(Q(owner=user))
    return books


def search_books(user, search_term):
    books = get_book(Book.objects, user)
    books = books.annotate(search=SearchVector(
        'title', 'author'
    ))
    books = books.filter(search=search_term).distinct('pk')
    return books
