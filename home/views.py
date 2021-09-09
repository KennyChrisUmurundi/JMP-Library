from django.shortcuts import render
from library.models import Library
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        libraries = Library.objects.filter(library_admin=request.user)
    else:
        libraries = None
    context = {"libraries": libraries}
    return render(request, "home/home.html", context)


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
