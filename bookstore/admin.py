from django.contrib import admin
from bookstore.models import Book, Author, Publisher
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
