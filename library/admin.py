from django.contrib import admin
from .models import Library, Catalog, Category, Ebook, Author, Member, Borrowed, Supplier, Purchase, Department, Designation, Employee, Media, Additional_library_information
# Register your models here.

admin.site.register(Library)
admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Borrowed)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Media)
admin.site.register(Additional_library_information)
