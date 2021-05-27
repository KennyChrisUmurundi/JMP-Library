from django.shortcuts import render
from library.models import Library

# Create your views here.

def home(request):
    return render(request,'home.html')

def libraries(request):
    admin = request.user
    print(admin)
    libraries = Library.objects.filter(library_admin = admin)
    print(libraries)
    context = {
    'libraries':libraries
    }
    return render(request,'libraries.html',context)
