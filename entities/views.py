from django.shortcuts import render, get_object_or_404
from .utilities import get_library
from library.models import Member, Library, Catalog, Ebook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import stripe
from django.http import JsonResponse
# Create your views here.


STRIPE_API_KEY = ''

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
    # library = Library.objects.filter(id=pk)
    catalogs = Catalog.objects.filter(library_id=pk)
    library     = Library.objects.filter(id=pk)
    
    query = request.GET.get('search')
    if query:

        queryset = (Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query))
        result = Catalog.objects.filter(queryset,library_id=pk).distinct()
        page = request.GET.get('page')
        paginator = Paginator(result,20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {

        'items':items,
        'query':query,
        'pk':pk,
        'libraries':library,
        # 'catalogs':catalogs,
        'paginator':page_obj
        }
        return render(request,'lib/items.html',context)
    else:

        page = request.GET.get('page')
        paginator = Paginator(catalogs,20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {

        'items':items,
        'pk':pk,
        'libraries':library,
        # 'catalogs':catalogs,
        'paginator':page_obj
        }
        return render(request,'lib/items.html',context)

def ebooks(request,pk):

    pk = pk
    library = Library.objects.filter(id=pk)
    ebooks = Ebook.objects.filter(library_id=pk)
    query = request.GET.get('search')
    library     = Library.objects.filter(id=pk)
    if query:

        queryset = (Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query))
        result = Ebook.objects.filter(queryset,library_id=pk).distinct()
        page = request.GET.get('page')
        paginator = Paginator(result,20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {

        'items':items,
        'query':query,
        'pk':pk,
        'libraries':library,
        # 'catalogs':catalogs,
        'paginator':page_obj
        }
        return render(request,'lib/items.html',context)
    else:

        page = request.GET.get('page')
        paginator = Paginator(ebooks,20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {

        'items':items,
        'pk':pk,
        'libraries':library,
        # 'catalogs':catalogs,
        'paginator':page_obj
        }
        return render(request,'lib/ebooks.html',context)


def single_ebook(request,pk,id):
    pk=pk 
    id = id 
    library  =   get_object_or_404(Library,id=pk)
    ebook  =   get_object_or_404(Ebook,id=id)
    ctx = {
    'library':library,
    'ebook':ebook,
    'pk':pk

    }
    return render(request,'lib/single_ebook.html',ctx)

def checkout(request):
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000,
                            'product_data': {
                                'name': 'Stubborn Attachments',
                                'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': 1,
                    },

                ],
                mode='payment',
                success_url='ebooks.html',
                cancel_url='ebooks.html',

            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse(error=str(e)), 403

