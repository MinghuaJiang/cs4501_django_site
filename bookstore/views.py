from django.shortcuts import render
from bookstore.models import Book
from bookstore.models import Publisher
from bookstore.models import Author
from django.http import JsonResponse


# Create your views here.


def get_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return JsonResponse({
        'ok': True,
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
    author = Author.objects.create(first_name=first_name, last_name=last_name, email=email)
    return JsonResponse({
        'ok': True,
        'result':
            {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'email': author.email
            }
    })


def get_publisher(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return JsonResponse({
        'ok': True,
        'result':
            {
                'name': publisher.name,
                'address': publisher.address,
                'city': publisher.city,
                'state_province': publisher.state_province,
                'country': publisher.country,
                'website': publisher.website
            }
    })


def create_publisher(request):
    name = request.POST['name']
    address = request.POST['address']
    city = request.POST['city']
    state_province = request.POST['state_province']
    country = request.POST['country']
    website = request.POST.get('website', '')
    publisher = Author.objects.create(name=name, address=address, city=city, state_province=state_province,
                                      country=country,
                                      website=website)
    return JsonResponse({
        'ok': True,
        'result':
            {
                'id': publisher.id,
                'name': publisher.name,
                'address': publisher.address,
                'city': publisher.city,
                'state_province': publisher.state_province,
                'country': publisher.country,
                'website': publisher.website
            }
    })


def get_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return JsonResponse({
        'ok': True,
        'result':
            {
                'title': book.title,
                'author': book.authors,
                'isbn': book.isbn,
                'publisher': book.publisher,
                'publication_date': book.publication_date,
                'edition': book.edition,
                'price': book.price,
                'discounted_price': book.discounted_price
            }
    })


def create_book(request):
    title = request.POST['title']
    author = request.POST['author']
    isbn = request.POST['isbn']
    publisher = request.POST['publisher']
    publication_date = request.POST['publication_date']
    edition = request.POST['edition']
    price = request.POST['price']
    discounted_price = request.POST['discounted_price']
    book = Book.objects.create(title=title, author=author, isbn=isbn, publisher=publisher,
                               publication_date=publication_date,
                               edition=edition, price=price, discounted_price=discounted_price)
    return JsonResponse({
        'ok': True,
        'result':
            {
                'id': book.id,
                'title': book.title,
                'author': book.authors,
                'isbn': book.isbn,
                'publisher': book.publisher,
                'publication_date': book.publication_date,
                'edition': book.edition,
                'price': book.price,
                'discounted_price': book.discounted_price
            }
    })
