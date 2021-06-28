from django.urls import path
from . import views


app_name    =  'entities'

urlpatterns =[
    path('<int:pk>/',views.lib,name='lib'),
    path('items/<int:pk>',views.items,name='items'),
    path('ebooks/<int:pk>',views.ebooks,name='ebooks'),
    path('ebook/<int:pk>/<int:id>',views.single_ebook,name='single_ebook'),
    path('Checkout',views.checkout,name='checkout'),

]
