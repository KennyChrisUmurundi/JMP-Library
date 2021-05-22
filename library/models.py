from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.urls import reverse

# Create your models here.

class Library(models.Model):

    library_admin       =       models.ForeignKey(User,on_delete=models.CASCADE)
    library_name        =       models.CharField(max_length=300)
    library_type        =       models.CharField(max_length=300)
    library_email       =       models.CharField(max_length=300)
    library_country     =       models.CharField(max_length=200,default='Others')

    def __str__(self):
        return self.library_name

    def get_absolute_url(self):
        return reverse('library:dashboard', kwargs={'pk': self.pk})

class Category(models.Model):

    library             =       models.ForeignKey(Library,on_delete=models.CASCADE)
    name                =       models.CharField(max_length=200)
    description         =       models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name


class Catalog(models.Model):

    library             =       models.ForeignKey(Library,on_delete=models.CASCADE)
    title               =       models.CharField(max_length=200)
    author              =       models.CharField(max_length=200)
    publisher           =       models.CharField(max_length=200)
    isbn                =       models.CharField(max_length=200,blank=True)
    issn                =       models.CharField(max_length=200,blank=True)
    call_no             =       models.CharField(max_length=200,blank=True)
    type                =       models.CharField(max_length=200,blank=True)
    category            =       models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    edition             =       models.CharField(max_length=200,blank=True)
    year                =       models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:catalog_items', kwargs={'pk': self.library.pk})

class Ebook(models.Model):

    library             = models.ForeignKey(Library,on_delete=models.CASCADE)
    title               = models.CharField(max_length=200)
    author              = models.CharField(max_length=200)
    publisher           = models.CharField(max_length=300)
    publication_year    = models.CharField(max_length=100)
    book_description    = models.TextField(null=True,blank=True)
    book_cover          = models.ImageField(upload_to='images',null=True,blank=True)
    book_pdf            = models.FileField(upload_to='books',null=False,blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:ebook_items', kwargs={'pk': self.library.pk})

class Author(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    name                =   models.CharField(max_length=200)
    country             =   models.CharField(max_length=200)
    year_born           =   models.CharField(max_length=200)
    year_died           =   models.CharField(max_length=200)
    bio                 =   models.TextField(null=True,blank=True)
    publications        =   models.TextField(null=True,blank=True)
    awards              =   models.TextField(null=True,blank=True)
    references          =   models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:authors', kwargs={'pk': self.library.pk})
