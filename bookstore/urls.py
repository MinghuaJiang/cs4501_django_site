from django.conf.urls import url
from bookstore.views import get_author
from bookstore.views import create_author

urlpatterns = [
    url(r'^api/v1/authors/(?P<author_id>\d+)$', get_author),
    url(r'^api/v1/authors/create$', create_author),
]
