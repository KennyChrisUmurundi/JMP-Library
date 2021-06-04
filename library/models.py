from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.

class Library(models.Model):

    library_admin       =       models.ForeignKey(User,on_delete=models.CASCADE)
    library_name        =       models.CharField(max_length=300)
    library_type        =       models.CharField(max_length=300)
    library_email       =       models.CharField(max_length=300)
    library_country     =       models.CharField(max_length=200,default='Others')
    library_phone       =       models.CharField(max_length=200,null=True,blank=True)

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
    description         =       models.TextField(null=True,blank=True)

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

class Member(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    first_name          =   models.CharField(max_length=200)
    last_name           =   models.CharField(max_length=200)
    member_no           =   models.CharField(unique=True,default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    image               =   models.ImageField(upload_to='images/profiles',null=True,blank=True)
    email               =   models.CharField(max_length=200)
    phone               =   models.CharField(max_length=200)
    address             =   models.CharField(max_length=200)
    status              =   models.CharField(max_length=200,default='Active')

    def __str__(self):
        return self.member_no

    def get_absolute_url(self):
        return reverse('library:members', kwargs={'pk': self.library.pk})

class Borrowed(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    catalog             =   models.CharField(max_length=200)
    member_no           =   models.CharField(max_length=200)
    day_borrowed        =   models.DateTimeField(default=timezone.now)
    due_return          =   models.DateTimeField()
    status              =   models.CharField(max_length=200,default='Not Returned')


    def get_absolute_url(self):
        return reverse('library:reports', kwargs={'pk': self.library.pk})

class Supplier(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    name                =   models.CharField(max_length=200)
    descripiton         =   models.TextField(null=True,blank=True)
    address             =   models.CharField(max_length=200)
    phone               =   models.CharField(max_length=200)
    email               =   models.CharField(max_length=200)
    country             =   models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:suppliers', kwargs={'pk': self.library.pk})

class Purchase(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    purchase_date       =   models.DateTimeField()
    title               =   models.CharField(max_length=200)
    supplier            =   models.ForeignKey(Supplier,on_delete=models.CASCADE)
    remark              =   models.TextField(null=True,blank=True)
    status              =   models.CharField(max_length=200)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:purchases', kwargs={'pk': self.library.pk})

class Designation(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    name                =   models.CharField(max_length=200)
    official_title      =   models.CharField(max_length=200)
    description         =   models.TextField(null=True,blank=True)
    status              =   models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:designation', kwargs={'pk': self.library.pk})

class Department(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    name                =   models.CharField(max_length=200)
    formal_name         =   models.CharField(max_length=200)
    descripiton         =   models.TextField(null=True,blank=True)
    type                =   models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:department', kwargs={'pk': self.library.pk})


class Employee(models.Model):

    library             =   models.ForeignKey(Library,on_delete=models.CASCADE)
    employee_no         =   models.CharField(unique=True,default=uuid.uuid4().hex[:4].upper(), max_length=50, editable=False)
    name                =   models.CharField(max_length=200)
    image               =   models.ImageField(upload_to='images',null=True,blank=True)
    designation         =   models.ForeignKey(Designation,on_delete=models.CASCADE)
    department          =   models.ForeignKey(Department,on_delete=models.CASCADE)
    remark              =   models.TextField(null=True,blank=True)
    status              =   models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:employee', kwargs={'pk': self.library.pk})
