from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("libraries/", views.libraries, name="libraries"),
    path("discover", views.discover, name="discover"),
    path("adapter", views.ussd_adapter, name="adapter"),
    path("site/management", views.saasperson, name="manage"),
]
