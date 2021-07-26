from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
]
