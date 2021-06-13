from django.shortcuts import render
from .utilities import get_library
from library.models import Member, Library, Catalog, Ebook
# Create your views here.

def lib(request,pk):
    pk          = pk
    library     = Library.objects.filter(id=pk)
    catalogs    = Catalog.objects.filter(library_id=pk)[0:4]
    ebook       = Ebook.objects.filter(library_id=pk)[0:4]
    context = {
    'pk':pk,
    'libraries':library,
    'catalogs':catalogs,
    'ebook':ebook,
    }

    return render(request,'lib/home.html',context)

def items(request,pk):

    pk = pk
    library = Library.objects.filter(id=pk)
    catalogs = Catalog.objects.filter(library_id=pk)
    context = {
    'pk':pk,
    'libraries':library,
    'catalogs':catalogs
    }
    return render(request,'lib/items.html',context)

def ebooks(request,pk):

    pk = pk
    library = Library.objects.filter(id=pk)
    ebooks = Ebook.objects.filter(library_id=pk)
    context = {
    'pk':pk,
    'libraries':library,
    'ebooks':ebooks
    }
    return render(request,'lib/items.html',context)
