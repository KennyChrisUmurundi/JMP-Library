from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddLibraryForm, AddCatalogForm, UpdateCatalogForm, AddEbookForm, UpdateEbookForm, AddCategoryForm, UpdateCategoryForm, AddAuthorForm, UpdateAuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Library, Catalog, Ebook, Category, Author
from django.views.generic.detail import SingleObjectMixin
# Create your views here.



def dashboard(request,pk):
    catalogs = Catalog.objects.filter(library=pk)
    context={
    'pk':pk,
    'catalogs':catalogs,
    }
    return render(request,'dashboard.html',context)

class CreateLibrary(LoginRequiredMixin,CreateView):

    model           =   Library
    form_class      =   AddLibraryForm
    template_name   =   'create_library.html'

    def form_valid(self,form):
        form.instance.library_admin = self.request.user
        return super(CreateLibrary,self).form_valid(form)

def CatalogItems(request,pk):
    pk=pk
    catalogs = Catalog.objects.filter(library=pk)
    library  = Library.objects.filter(pk=pk)
    context = {
    'pk':pk,
    'catalogs':catalogs,
    'library':library
    }
    return render(request,'catalogItems.html',context)

def EbookItems(request,pk):
    pk=pk
    Ebooks = Ebook.objects.filter(library=pk)

    context = {
    'pk':pk,
    'ebooks':Ebooks,

    }
    return render(request,'ebook_items.html',context)

def addEbook(request,pk):

    pk=pk
    if request.method == 'POST':
        form    =   AddEbookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.library_id = pk
            print(ebook.library_id)
            ebook.save()
            return redirect('library:ebook_items',pk=pk)
    form = AddEbookForm()
    context = {
    'form':form,
    'pk':pk,

    }
    return render(request,'create_ebook.html',context)

class UpdateEbook(LoginRequiredMixin,UpdateView):

    model = Ebook
    template_name = 'update_ebook.html'
    form_class  = UpdateEbookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context

def DeleteEbook(request,id):

    object  =   get_object_or_404(Ebook,id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect('library:ebook_items',pk=object.library_id)


def addCatalog(request,pk):
    library  = Library.objects.filter(pk=pk)
    pk=pk
    if request.method == 'POST':
        form    =   AddCatalogForm(request.POST)
        if form.is_valid():
            catalog = form.save(commit=False)
            catalog.library_id = pk
            print(catalog)
            catalog.save()
            return redirect('library:catalog_items',pk=pk)
    form = AddCatalogForm()
    context = {
    'form':form,
    'pk':pk,
    'library':library
    }
    return render(request,'add_catalog.html',context)

class UpdateCatalog(LoginRequiredMixin,UpdateView):

    model = Catalog
    template_name = 'update_catalog.html'
    form_class  = UpdateCatalogForm
    pk  =   'object.pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context

def DeleteCatalog(request,id):

    object  =   get_object_or_404(Catalog,id=id)
    print(object.library_id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect('library:catalog_items',pk=object.library_id)

def Categories(request,pk):

    pk=pk
    categories = Category.objects.filter(library=pk)
    library  = Library.objects.filter(pk=pk)
    context = {
    'pk':pk,
    'category':categories,
    'library':library
    }
    return render(request,'category.html',context)

def addCategory(request,pk):

    pk=pk
    if request.method == 'POST':
        form    =   AddCategoryForm(request.POST)
        if form.is_valid():
            catalog = form.save(commit=False)
            catalog.library_id = pk
            print(catalog)
            catalog.save()
            return redirect('library:categories',pk=pk)
    form = AddCategoryForm()
    context = {
    'form':form,
    'pk':pk,

    }
    return render(request,'add_category.html',context)

class UpdateCategory(LoginRequiredMixin,UpdateView):

    model = Category
    template_name = 'update_catalog.html'
    form_class  = UpdateCategoryForm
    pk  =   'object.pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context

def DeleteCategory(request,id):

    object  =   get_object_or_404(Category,id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect('library:categories',pk=object.library_id)

def authors(request,pk):

    pk=pk
    authors = Author.objects.filter(library=pk)

    context = {
    'pk':pk,
    'authors':authors,

    }
    return render(request,'authors.html',context)

def addAuthor(request,pk):

    pk=pk
    if request.method == 'POST':
        form    =   AddAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.library_id = pk
            author.save()
            return redirect('library:authors',pk=pk)
    form = AddAuthorForm()
    context = {
    'form':form,
    'pk':pk,

    }
    return render(request,'add_authors.html',context)

class UpdateAuthor(LoginRequiredMixin,UpdateView):

    model = Author
    template_name = 'update_author.html'
    form_class  = UpdateAuthorForm
    pk  =   'object.pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context

def DeleteAuthor(request,id):

    object  =   get_object_or_404(Author,id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect('library:authors',pk=object.library_id)
