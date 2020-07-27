from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import BookViewSet, api_root, NoteViewSet
from rest_framework import renderers


book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
note_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
note_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', api_root),
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('notes/', note_list, name='note-list'),
    path('notes/<int:pk>/', note_detail, name='note-detail'),
    
]


urlpatterns = format_suffix_patterns(urlpatterns)