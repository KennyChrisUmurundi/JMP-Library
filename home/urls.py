from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path('',views.home,name='home'),
    path('libraries/',views.libraries, name='libraries'),
    path('discover',views.discover,name='discover')
]
