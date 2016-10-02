from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
# To-do add user and review
# Add book category
# Add book language


@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    edition = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    discounted_price = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return u'%s; %s edition (%s)' % (self.title, self.edition, self.publication_date)

