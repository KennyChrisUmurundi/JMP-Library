from django.shortcuts import render
from .utilities import get_library
from library.models import Member, Library, Catalog
# Create your views here.

def lib(request,pk):
    pk = pk
    library = Library.objects.filter(id=pk)

    context = {
    'pk':pk,
    'library':library
    }
    return render(request,'lib/home.html',context)

def items(request,pk):

    pk = pk
    library = Library.objects.filter(id=pk)
    catalogs = Catalog.objects.filter(library_id=pk)
    context = {
    'pk':pk,
    'library':library,
    'catalogs':catalogs
    }
    return render(request,'lib/items.html',context)
