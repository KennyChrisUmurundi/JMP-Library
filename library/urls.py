from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [

    # DASHBOARD
    path('dashboard/<int:pk>/',views.dashboard,name="dashboard"),

    # ADD LIBRARY
    path('new_library/',views.CreateLibrary.as_view(),name='create_library'),
    path('update_library/<int:pk>',views.UpdateLibrary.as_view(),name='update_library'),
    # path('create_category/',views.create_category,name='create_category'),

    # CATALOGS
    path('items/<int:pk>/',views.CatalogItems,name='catalog_items'),
    path('add_catalog/<int:pk>/',views.addCatalog,name='add_catalog'),
    path('update_catalog/<int:pk>/',views.UpdateCatalog.as_view(),name='update_catalog'),
    path('delete_catalog/<int:id>/',views.DeleteCatalog,name='delete_catalog'),

    # EBOOKS
    path('ebook_items/<int:pk>/',views.EbookItems,name='ebook_items'),
    path('add_ebook/<int:pk>/',views.addEbook,name='add_ebook'),
    path('update_ebook/<int:pk>/',views.UpdateEbook.as_view(),name='update_ebook'),
    path('delete_ebook/<int:id>/',views.DeleteEbook,name='delete_ebook'),

    # Categories

    path('categories/<int:pk>/',views.Categories,name='categories'),
    path('add_category/<int:pk>/',views.addCategory,name='add_category'),
    path('update_category/<int:pk>/',views.UpdateCategory.as_view(),name='update_category'),
    path('delete_category/<int:id>/',views.DeleteCategory,name='delete_category'),

    # Authors

    path('authors/<int:pk>/',views.authors,name='authors'),
    path('add_author/<int:pk>/',views.addAuthor,name='add_author'),
    path('update_author/<int:pk>/',views.UpdateAuthor.as_view(),name='update_author'),
    path('delete_author/<int:id>/',views.DeleteAuthor,name='delete_author'),

    # Members

    path('members/<int:pk>/',views.members,name='members'),
    path('add_member/<int:pk>/',views.addMember,name='add_member'),
    path('update_member/<int:pk>/',views.UpdateMember.as_view(),name='update_member'),
    path('delete_member/<int:id>/',views.DeleteMember,name='delete_member'),

    # Borrowing

    path('borrow/<int:pk>',views.Borrow,name='borrow'),
    path('items/<int:pk>',views.register_borrower,name='register_borrower'),
    path('reports/<int:pk>',views.borrow_report,name='reports'),
    path('Checkout/<int:pk>/',views.Checkout.as_view(),name='checkout'),
    path('over_due/<int:pk>',views.over_due,name='over_due'),

    # Suppliers

    path('suppliers/<int:pk>',views.suppliers,name='suppliers'),
    path('add_suppliers/<int:pk>/',views.add_suppliers,name='add_suppliers'),
    path('update_supplier/<int:pk>/',views.UpdateSupplier.as_view(),name='update_supplier'),
    path('delete_supplier/<int:id>/',views.DeleteSupplier,name='delete_supplier'),


    # Purchases

    path('purchases/<int:pk>',views.purchases,name='purchases'),
    path('add_purchases/<int:pk>/',views.add_purchase,name='add_purchase'),
    # path('update_purchase/<int:pk>/',views.UpdatePurchase.as_view(),name='update_purchase'),
    path('delete_purchase/<int:id>/',views.DeletePurchase,name='delete_purchase'),

    # Employees

    path('employees/<int:pk>',views.employees,name='employee'),
    path('add_employee/<int:pk>/',views.add_employee,name='add_employee'),
    path('update_employee/<int:pk>/',views.UpdateEmployee.as_view(),name='update_employee'),
    path('delete_employee/<int:id>/',views.DeleteEmployee,name='delete_employee'),

    # Designations

    path('designations/<int:pk>',views.designations,name='designation'),
    path('add_designation/<int:pk>/',views.add_designation,name='add_designation'),
    path('update_designation/<int:pk>/',views.UpdateDesignation.as_view(),name='update_designation'),
    path('delete_designation/<int:id>/',views.DeleteDesignation,name='delete_designation'),

    # Department

    path('department/<int:pk>',views.department,name='department'),
    path('add_department/<int:pk>/',views.add_department,name='add_department'),
    path('update_department/<int:pk>/',views.UpdateDepartment.as_view(),name='update_department'),
    path('delete_department/<int:id>/',views.DeleteDepartment,name='delete_department'),


    # Media
    path('media_mp3/<int:pk>',views.media_mp3,name='media_mp3'),
    path('media_video/<int:pk>',views.media_video,name='media_video'),
    path('add_mp3/<int:pk>/',views.add_mp3,name='add_mp3'),
    path('add_video/<int:pk>/',views.add_video,name='add_video'),
    path('update_mp3/<int:pk>/',views.UpdateMp3.as_view(),name='update_mp3'),
    path('update_video/<int:pk>/',views.UpdateVideo.as_view(),name='update_video'),
    path('delete_media/<int:id>/',views.DeleteMedia,name='delete_media'),

    # Event
    path('event/<int:pk>',views.event,name='event'),
    path('add_event/<int:pk>/',views.add_event,name='add_event'),
    # path('update_event/<int:pk>/',views.UpdateMedia.as_view(),name='update_event'),
    # path('delete_event/<int:id>/',views.DeleteMedia,name='delete_event'),

    # Plans

    path('plan/<int:pk>',views.plan,name='plan'),
    path('process_subscription/<plan>/<int:pk>', views.process_subscription, name='process_subscription'),




]
