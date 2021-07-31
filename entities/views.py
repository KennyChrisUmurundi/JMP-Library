from django.shortcuts import render, get_object_or_404, redirect
from .utilities import get_library
from library.models import Member, Library, Catalog, Ebook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.db.models import Q
from django.conf import settings
import stripe
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import bought_items
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from account.forms import UserRegisterForm

# Create your views here.


# stripe.api_key = settings.STRIPE_PRIVATE_KEY

logger = logging.getLogger(__name__)



class library_login(LoginView):
    template_name = "auth/login.html"

def library_login(request,path):    
    path = path
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print("nakuonaaa")
        if user is not None:
            login(request, user)
            return redirect(path)
            print("egoooo")
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            print("wapiiiiii")
            # messages.warning(request, 'Username or Password Incorrect!')
            return redirect(path)

    return render(request,'auth/login.html',{'path':path})

def account_register(request,path):
    path = path
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("logged on succesfully")
                login(request, user)
                return redirect(path)
            else:
                print("bado")
                return HttpResponseRedirect(reverse("account:login"))
            login(request, user)
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect(path)
    else:
        form =  UserRegisterForm()
    return render(request, "auth/register.html", {"form": form,'path':path})

def lib(request, pk):
    pk = pk
    library = Library.objects.filter(id=pk)
    catalogs = Catalog.objects.filter(library_id=pk)[0:4]
    ebook = Ebook.objects.filter(library_id=pk)[0:4]
    context = {
        "pk": pk,
        "libraries": library,
        "catalogs": catalogs,
        "ebook": ebook,
    }

    return render(request, "lib/home.html", context)


def items(request, pk):

    pk = pk
    # library = Library.objects.filter(id=pk)
    catalogs = Catalog.objects.filter(library_id=pk)
    library = Library.objects.filter(id=pk)

    query = request.GET.get("search")
    if query:

        queryset = (
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(publisher__icontains=query)
        )
        result = Catalog.objects.filter(queryset, library_id=pk).distinct()
        page = request.GET.get("page")
        paginator = Paginator(result, 4)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {
            "items": items,
            "query": query,
            "pk": pk,
            "libraries": library,
            # 'catalogs':catalogs,
            "paginator": page_obj,
        }
        return render(request, "lib/items.html", context)
    else:

        page = request.GET.get("page")
        paginator = Paginator(catalogs, 12)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {
            "items": items,
            "pk": pk,
            "libraries": library,
            # 'catalogs':catalogs,
            "paginator": page_obj,
        }
        return render(request, "lib/items.html", context)


def ebooks(request, pk):

    pk = pk
    library = Library.objects.filter(id=pk)
    ebooks = Ebook.objects.filter(library_id=pk)
    query = request.GET.get("search")
    library = Library.objects.filter(id=pk)
    if query:

        queryset = (
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(publisher__icontains=query)
        )
        result = Ebook.objects.filter(queryset, library_id=pk).distinct()
        page = request.GET.get("page")
        paginator = Paginator(result, 20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {
            "items": items,
            "query": query,
            "pk": pk,
            "libraries": library,
            # 'catalogs':catalogs,
            "paginator": page_obj,
        }
        return render(request, "lib/ebooks.html", context)
    else:

        page = request.GET.get("page")
        paginator = Paginator(ebooks, 20)
        page_obj = paginator.get_page(page)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {
            "items": items,
            "pk": pk,
            "libraries": library,
            # 'catalogs':catalogs,
            "paginator": page_obj,
        }
        return render(request, "lib/ebooks.html", context)


def single_ebook(request, pk, id):
    pk = pk
    id = id
    library = get_object_or_404(Library, id=pk)
    ebook = get_object_or_404(Ebook, id=id)
    ctx = {"library": library, "ebook": ebook, "pk": pk}
    return render(request, "lib/single_ebook.html", ctx)


# def checkout(request, id, pk):
#     pk = pk
#     print("seeing you")
#     library = Library.objects.get(id=id)

#     session = stripe.checkout.Session.create(
#         payment_method_types=["card"],
#         line_items=[
#             {
#                 "price": "price_1J8UOiEb6vVsn22vNYHKiyVc",
#                 "quantity": 1,
#             }
#         ],
#         mode="payment",
#         success_url=request.build_absolute_uri(
#             reverse("entities:ebooks", kwargs={"pk": library, "pk": pk})
#         )
#         + "?session_id={CHECKOUT_SESSION_ID}",
#         cancel_url=request.build_absolute_uri(
#             reverse("entities:ebooks", kwargs={"pk": library, "pk": pk})
#         ),
#     )

#     return JsonResponse(
#         {"session_id": session.id, "stripe_public_key": settings.STRIPE_PUBLIC_KEY}
#     )

@csrf_exempt
def paypal_webhook(request):
    jsondata = request.body
    data = json.loads(jsondata)
    # purchase = data.get("resource")
    # status = purchase["status"]
    # details = purchase["payer"]["email_address"]
    # print(details,'aaaaaaaaaaannnnnnnd','aaaaaaaaaaand',status)
    # print(book)
    print("daaaaaaaataaaaaaaa",data)
    logger.debug("Thissssssssss  :%s" % data)
    return HttpResponse(status=200)

def complete_order(request):
    body = json.loads(request.body)
    print('The Bodyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',body)

    item = Ebook.objects.get(id=body['productId'])
    library = Library.objects.get(id=body['library'])
    bought_items.objects.create(
        buyer=request.user,
        item = item.title,
        item_file=item.book_pdf,
        ebook = item,
        library=library
        )
    return JsonResponse('Payment Complete',safe=False)


def my_books(request,pk):
    pk = pk
    lib= Library.objects.get(id=pk)
    libra = Library.objects.filter(id=pk)
    my_book = bought_items.objects.filter(buyer=request.user,library=lib)

    ctx = {
        'my_book':my_book,
        'libraries':libra,
        'pk':pk
    }
    return render(request,'lib/my_books.html',ctx)


