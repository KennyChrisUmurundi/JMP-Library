from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [

    # DASHBOARD
    # path('dashboard/<int:pk>/',views.dashboard,name="dashboard"),
    #
    # # ADD LIBRARY
    # path('new_library/',views.CreateLibrary.as_view(),name='create_library'),
    #
    # # CATALOGS
    # path('items/<int:pk>/',views.CatalogItems,name='catalog_items'),
    # path('add_catalog/<int:pk>/',views.addCatalog,name='add_catalog'),
    # path('update_catalog/<int:pk>/',views.UpdateCatalog.as_view(),name='update_catalog'),
    # path('delete_catalog/<int:id>/',views.DeleteCatalog,name='delete_catalog'),
    #
    # # EBOOKS
    # path('ebook_items/<int:pk>/',views.EbookItems,name='ebook_items'),
    # path('add_ebook/<int:pk>/',views.addEbook,name='add_ebook'),
    # path('update_ebook/<int:pk>/',views.UpdateEbook.as_view(),name='update_ebook'),
    # path('delete_ebook/<int:id>/',views.DeleteEbook,name='delete_ebook'),
    #
    # # Categories
    #
    # path('categories/<int:pk>/',views.Categories,name='categories'),
    # path('add_category/<int:pk>/',views.addCategory,name='add_category'),
    # path('update_category/<int:pk>/',views.UpdateCategory.as_view(),name='update_category'),
    # path('delete_category/<int:id>/',views.DeleteCategory,name='delete_category'),
    #
    # # Authors
    #
    # path('authors/<int:pk>/',views.authors,name='authors'),
    # path('add_author/<int:pk>/',views.addAuthor,name='add_author'),
    # path('update_author/<int:pk>/',views.UpdateAuthor.as_view(),name='update_author'),
    # path('delete_author/<int:id>/',views.DeleteAuthor,name='delete_author'),



]
