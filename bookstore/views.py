from django.shortcuts import render
from bookstore.models import Book
from bookstore.models import Publisher
from bookstore.models import Author
from django.http import JsonResponse

# Create your views here.


def get_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return JsonResponse({
        'ok':     True,
        'result':
        {
            'first_name': author.first_name,
            'last_name': author.last_name,
            'email': author.email
        }
    })


def create_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST.get('email', '')
    author = Author.objects.create(first_name=first_name,last_name=last_name, email=email)
    return JsonResponse({
        'ok':     True,
        'result':
        {
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'email': author.email
        }
    })


def get_book(request):
    book = Book.objects.filter()
    return JsonResponse({
        'ok':     True,
        'result':
        {
            'title':    book.title,
            'author':   book.authors,
            'publisher': book.publisher,
            'publication_date': book.publication_date,
            'publication_version': book.publication_version
        }
    })

