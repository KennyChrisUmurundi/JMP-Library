from django.urls import path
from . import views


app_name    =  'entities'

urlpatterns =[
    path('<int:pk>/',views.lib,name='lib'),
    path('items/<int:pk>',views.items,name='items')

]
