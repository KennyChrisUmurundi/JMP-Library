from django.contrib import admin
from .models import Library, Catalog, Category, Ebook, Author
# Register your models here.

admin.site.register(Library)
admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Author)
