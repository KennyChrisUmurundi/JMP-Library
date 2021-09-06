from django.urls import path
from . import views


app_name = "entities"

urlpatterns = [
    path("<int:pk>/", views.lib, name="lib"),
    path("items/<int:pk>", views.items, name="items"),
    path("ebooks/<int:pk>", views.ebooks, name="ebooks"),
    path("ebook/<int:pk>/<int:id>", views.single_ebook, name="single_ebook"),
    # path("checkout", views.checkout, name="checkout"),
<<<<<<< HEAD
    path("Paypal-Webhook",views.paypal_webhook,name='webhook'),
=======
    path("Paypal-Webhook/",views.paypal_webhook,name='webhook'),
>>>>>>> 6ec18b616131222795b3af768106d831d3c133ad
    path("complete_order",views.complete_order,name="complete_order"),
    path("login/<path:path>",views.library_login,name="login"),
    path("register/<path:path>",views.account_register,name="register"),
    path("My Books/<int:pk>",views.my_books,name='my_book'),
    path("Music/<int:pk>",views.mp3,name='music'),
    path("Videos/<int:pk>",views.video,name='video'),


]
