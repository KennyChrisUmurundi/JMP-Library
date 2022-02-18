from django.shortcuts import render
from library.models import Library
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

host = settings.ALLOWED_HOSTS


def home(request):
    jmp = "jmplibrary.com"
    county = "county.solutions"
    hosting = None
    print(host)
    if jmp in host:
        hosting = "family archiving opportunities, businesses,and more"
    elif county in host:
        hosting = "county governments"

    return render(request, "home/home.html", {"aliwigs": hosting})


def libraries(request):
    admin = request.user
    print(admin)
    libraries = Library.objects.filter(library_admin=admin)
    print(libraries)
    context = {"libraries": libraries}
    return render(request, "home/libraries.html", context)


def discover(request):

    library = Library.objects.all().order_by("?")[:12]

    # if Library.objects.filter(library_type = 'Entertainment'):
    #     img = 'img/librry_default.jpeg'

    ctx = {
        # 'img':img,
        "libraries": library
    }
    return render(request, "home/discover.html", ctx)


def ussd_adapter(request):
    bank = "123123123"
    return JsonResponse({"bank": bank})


def saasperson(request):
    return render(request, "home/saasgerant.html")
