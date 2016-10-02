from django.conf.urls import url
from bookstore.views import *

urlpatterns = [
    url(r'^api/v1/authors/(?P<author_id>\d+)$', get_author),
    url(r'^api/v1/publishers/(?P<publisher_id>\d+)$', get_publisher),
    url(r'^api/v1/books/(?P<book_id>\d+)$', get_book),
    url(r'^api/v1/authors/create$', create_author),
    url(r'^api/v1/publishers/create$', create_publisher),
    url(r'^api/v1/books/create$', create_book),
]
