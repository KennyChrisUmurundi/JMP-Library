from django.http.response import HttpResponse
import datetime
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
)
from .forms import (
    AddLibraryForm,
    AddCatalogForm,
    UpdateCatalogForm,
    AddEbookForm,
    UpdateEbookForm,
    AddCategoryForm,
    UpdateCategoryForm,
    AddAuthorForm,
    UpdateAuthorForm,
    AddMemberForm,
    UpdateMemberForm,
    AddBorrowForm,
    CheckoutForm,
    AddSupplierForm,
    AddPurchaseForm,
    UpdateSupplierForm,
    UpdatePurchaseForm,
    AddEmployeeForm,
    UpdateEmployee,
    AddDesignationForm,
    UpdateDesignation,
    AddDepartmentForm,
    UpdateDepartment,
    AddMediaForm,
    UpdateMedia,
    UpdateLibraryForm,
    AddMp3Form,
    AddVideoForm,
    UpdateMp3Form,
    UpdateMp3Form,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import (
    Library,
    Catalog,
    Ebook,
    Category,
    Author,
    Member,
    Borrowed,
    Supplier,
    Purchase,
    Employee,
    Designation,
    Department,
    Media,
    Event,
)
from django.views.generic.detail import SingleObjectMixin
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import user_passes_test

# from entities.models import Entity
# Create your views here.


def is_library_admin(user):
    try:
        library = Library.objects.get(library_admin=user)
        print(library, library.is_still_active, library.paid_until)
        if library and library.paid_until:
            if (
                library
                and library.is_still_active
                and library.paid_until >= datetime.date.today()
            ):
                return True
            elif library and library.paid_until < datetime.date.today():
                library.is_still_active = False
                library.plan = library.BASIC
                library.save()
                return False
        else:
            if library and library.is_still_active:
                return True
            else:
                return False

    except Library.DoesNotExist:
        return False


# @user_passes_test(is_library_admin)
def dashboard(request, pk):
    catalogs = Catalog.objects.filter(library=pk)
    libraries = Library.objects.filter(id=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    # library = Library.objects.get(id=pk)
    context = {
        "pk": pk,
        "catalogs": catalogs,
        "libraries": libraries,
        "library": library,
    }
    return render(request, "dashboard.html", context)


class UpdateLibrary(LoginRequiredMixin, UpdateView):

    model = Library
    template_name = "library_info/additional_library_infos.html"
    form_class = UpdateLibraryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        context["library"] = Library.objects.get(id=con)
        return context


class CreateLibrary(LoginRequiredMixin, CreateView):

    model = Library
    form_class = AddLibraryForm
    template_name = "create_library.html"

    def form_valid(self, form):
        check = None
        try:
            check = Library.objects.get(library_admin=self.request.user)
        except Library.DoesNotExist:
            pass
        if check:
            return render(
                self.request,
                template_name="create_library.html",
            )
        else:
            form.instance.library_admin = self.request.user
            date = datetime.date.today()
            print(date)
            print(date + datetime.timedelta(30))
            form.instance.paid_until = date + datetime.timedelta(30)
            return super(CreateLibrary, self).form_valid(form)


# def create_category(request):
#     return render(request,'category_select.html')


@user_passes_test(is_library_admin)
def CatalogItems(request, pk):
    pk = pk
    catalogs = Catalog.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    context = {"pk": pk, "catalogs": catalogs, "library": library}
    return render(request, "catalog/catalogItems.html", context)


@user_passes_test(is_library_admin)
def EbookItems(request, pk):
    pk = pk
    Ebooks = Ebook.objects.filter(library=pk)

    context = {
        "pk": pk,
        "ebooks": Ebooks,
        "library": Library.objects.get(id=pk),
    }
    return render(request, "ebook/ebook_items.html", context)


@user_passes_test(is_library_admin)
def addEbook(request, pk):

    pk = pk
    if request.method == "POST":
        form = AddEbookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.library_id = pk
            print(ebook.library_id)
            ebook.save()
            return redirect("library:ebook_items", pk=pk)
    form = AddEbookForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "ebook/create_ebook.html", context)


class UpdateEbook(LoginRequiredMixin, UpdateView):

    model = Ebook
    template_name = "ebook/update_ebook.html"
    form_class = UpdateEbookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        context["library"] = Library.objects.get(id=con)
        return context


@user_passes_test(is_library_admin)
def DeleteEbook(request, id):

    object = get_object_or_404(Ebook, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:ebook_items", pk=object.library_id)


@user_passes_test(is_library_admin)
def addCatalog(request, pk):
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    pk = pk
    if request.method == "POST":
        form = AddCatalogForm(request.POST)
        if form.is_valid():
            catalog = form.save(commit=False)
            catalog.library_id = pk
            print(catalog)
            catalog.save()
            return redirect("library:catalog_items", pk=pk)
    form = AddCatalogForm()
    context = {"form": form, "pk": pk, "library": library}
    return render(request, "catalog/add_catalog.html", context)


class UpdateCatalog(LoginRequiredMixin, UpdateView):

    model = Catalog
    template_name = "catalog/update_catalog.html"
    form_class = UpdateCatalogForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        context["library"] = Library.objects.get(id=con)
        return context


@user_passes_test(is_library_admin)
def DeleteCatalog(request, id):

    object = get_object_or_404(Catalog, id=id)
    print(object.library_id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:catalog_items", pk=object.library_id)


@user_passes_test(is_library_admin)
def Categories(request, pk):

    pk = pk
    categories = Category.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    context = {"pk": pk, "category": categories, "library": library}
    return render(request, "category/category.html", context)


@user_passes_test(is_library_admin)
def addCategory(request, pk):

    pk = pk
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.library_id = pk
            print(category)
            category.save()
            return redirect("library:categories", pk=pk)
    form = AddCategoryForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "category/add_category.html", context)


class UpdateCategory(LoginRequiredMixin, UpdateView):

    model = Category
    template_name = "category/update_category.html"
    form_class = UpdateCategoryForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        context["library"] = Library.objects.get(id=con)
        return context


@user_passes_test(is_library_admin)
def DeleteCategory(request, id):

    object = get_object_or_404(Category, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:categories", pk=object.library_id)


@user_passes_test(is_library_admin)
def authors(request, pk):

    pk = pk
    authors = Author.objects.filter(library=pk)

    context = {
        "pk": pk,
        "authors": authors,
        "library": Library.objects.get(id=pk),
    }
    return render(request, "authors/authors.html", context)


@user_passes_test(is_library_admin)
def addAuthor(request, pk):

    pk = pk
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.library_id = pk
            author.save()
            return redirect("library:authors", pk=pk)
    form = AddAuthorForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "authors/add_authors.html", context)


class UpdateAuthor(LoginRequiredMixin, UpdateView):

    model = Author
    template_name = "authors/update_author.html"
    form_class = UpdateAuthorForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        context["library"] = Library.objects.get(id=con)
        return context


@user_passes_test(is_library_admin)
def DeleteAuthor(request, id):

    object = get_object_or_404(Author, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:authors", pk=object.library_id)


@user_passes_test(is_library_admin)
def members(request, pk):

    pk = pk
    members = Member.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "members": members, "library": library}
    return render(request, "member/members_list.html", context)


@user_passes_test(is_library_admin)
def addMember(request, pk):

    pk = pk
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.library_id = pk
            member.save()
            return redirect("library:members", pk=pk)
    form = AddMemberForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "member/add_member.html", context)


class UpdateMember(LoginRequiredMixin, UpdateView):

    model = Member
    template_name = "member/update_member.html"
    form_class = UpdateMemberForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def DeleteMember(request, id):

    object = get_object_or_404(Member, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:members", pk=object.library_id)


@user_passes_test(is_library_admin)
def Borrow(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddBorrowForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.library_id = pk
            member = Member.objects.filter(
                member_no=item.member_no, library_id=pk
            )
            if member.exists():
                item.save()
                return redirect("library:reports", pk=pk)
            else:
                print("ntabaho")
            return redirect("library:reports", pk=pk)
    form = AddBorrowForm()
    context = {"form": form, "pk": pk, "library": Library.objects.get(id=pk)}
    return render(request, "borrow/borrow.html", context)


@user_passes_test(is_library_admin)
def register_borrower(request, pk):
    pk = pk
    catalogs = Catalog.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    context = {"pk": pk, "catalogs": catalogs, "library": library}
    return render(request, "borrow/register_borrower.html", context)


@user_passes_test(is_library_admin)
def borrow_report(request, pk):
    pk = pk
    catalogs = Catalog.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    borrowed = Borrowed.objects.filter(library=pk)
    checked_out = Borrowed.objects.filter(status="Not Returned")
    print(checked_out)
    context = {
        "pk": pk,
        "catalogs": catalogs,
        "library": library,
        "borrowed": borrowed,
        "checked_out": checked_out,
    }
    return render(request, "borrow/report.html", context)


class Checkout(LoginRequiredMixin, UpdateView):

    model = Borrowed
    template_name = "borrow/checkout.html"
    form_class = CheckoutForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def over_due(request, pk):
    pk = pk
    catalogs = Catalog.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    borrowed = Borrowed.objects.filter(library=pk)
    # checked_out =   Borrowed.objects.filter(status='Not Returned')
    # print(checked_out)
    context = {
        "pk": pk,
        "catalogs": catalogs,
        "library": library,
        "borrowed": borrowed,
        # 'checked_out':checked_out
    }
    return render(request, "borrow/over_due.html", context)


@user_passes_test(is_library_admin)
def suppliers(request, pk):

    pk = pk
    suppliers = Supplier.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "suppliers": suppliers, "library": library}
    return render(request, "supplier/supplier.html", context)


@user_passes_test(is_library_admin)
def add_suppliers(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.library_id = pk
            supplier.save()
            return redirect("library:suppliers", pk=pk)
    form = AddSupplierForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "supplier/add_suppliers.html", context)


class UpdateSupplier(LoginRequiredMixin, UpdateView):

    model = Supplier
    template_name = "supplier/update_supplier.html"
    form_class = UpdateSupplierForm
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def DeleteSupplier(request, id):

    object = get_object_or_404(Supplier, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:supliers", pk=object.library_id)


@user_passes_test(is_library_admin)
def purchases(request, pk):

    pk = pk
    purchases = Purchase.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "purchases": purchases, "library": library}
    return render(request, "purchase/purchases.html", context)


# class UpdatePurchase(LoginRequiredMixin,UpdateView):

#     model = Purchase
#     template_name = 'purchase/add_purchase.html'
#     form_class  = UpdatePurchaseForm
#     pk  =   'object.pk'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         con = self.object.pk
#         context["pk"] = con
#         return context


@user_passes_test(is_library_admin)
def add_purchase(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddPurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.library_id = pk
            purchase.save()
            return redirect("library:purchases", pk=pk)
    form = AddPurchaseForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "purchase/add_purchase.html", context)


@user_passes_test(is_library_admin)
def DeletePurchase(request, id):

    object = get_object_or_404(Purchase, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:purchases", pk=object.library_id)


@user_passes_test(is_library_admin)
def employees(request, pk):

    pk = pk
    employees = Employee.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "employees": employees, "library": library}
    return render(request, "employee/employee.html", context)


class UpdateEmployee(LoginRequiredMixin, UpdateView):

    model = Employee
    template_name = "employee/update_employee.html"
    form_class = UpdateEmployee
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def add_employee(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.library_id = pk
            employee.save()
            return redirect("library:employee", pk=pk)
    form = AddEmployeeForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "employee/add_employee.html", context)


@user_passes_test(is_library_admin)
def DeleteEmployee(request, id):

    object = get_object_or_404(Employee, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:employee", pk=object.library_id)


@user_passes_test(is_library_admin)
def designations(request, pk):

    pk = pk
    designations = Designation.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "designations": designations, "library": library}
    return render(request, "designation/designation.html", context)


class UpdateDesignation(LoginRequiredMixin, UpdateView):

    model = Designation
    template_name = "designation/update_designation.html"
    form_class = UpdateDesignation
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def add_designation(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddDesignationForm(request.POST)
        if form.is_valid():
            designation = form.save(commit=False)
            designation.library_id = pk
            designation.save()
            return redirect("library:designation", pk=pk)
    form = AddDesignationForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "designation/add_designation.html", context)


@user_passes_test(is_library_admin)
def DeleteDesignation(request, id):

    object = get_object_or_404(Designation, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:designation", pk=object.library_id)


@user_passes_test(is_library_admin)
def department(request, pk):

    pk = pk
    departments = Department.objects.filter(library=pk)
    library = get_object_or_404(Library, id=pk, library_admin=request.user)

    context = {"pk": pk, "departments": departments, "library": library}
    return render(request, "department/department.html", context)


class UpdateDepartment(LoginRequiredMixin, UpdateView):

    model = Department
    template_name = "department/update_department.html"
    form_class = UpdateDepartment
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def add_department(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.library_id = pk
            department.save()
            return redirect("library:department", pk=pk)
    form = AddDepartmentForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "department/add_department.html", context)


@user_passes_test(is_library_admin)
def DeleteDepartment(request, id):

    object = get_object_or_404(Department, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:department", pk=object.library_id)


@user_passes_test(is_library_admin)
def media_mp3(request, pk):

    pk = pk
    media = Media.objects.filter(library=pk)

    context = {
        "pk": pk,
        "media": media,
        "library": get_object_or_404(
            Library, id=pk, library_admin=request.user
        ),
    }
    return render(request, "media/mp3.html", context)


@user_passes_test(is_library_admin)
def media_video(request, pk):

    pk = pk
    media = Media.objects.filter(library=pk)

    context = {
        "pk": pk,
        "media": media,
        "library": get_object_or_404(
            Library, id=pk, library_admin=request.user
        ),
    }
    return render(request, "media/video.html", context)


class UpdateMp3(LoginRequiredMixin, UpdateView):

    model = Media
    template_name = "media/add_mp3.html"
    form_class = UpdateMedia
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


class UpdateVideo(LoginRequiredMixin, UpdateView):

    model = Media
    template_name = "media/add_video.html"
    form_class = UpdateMedia
    pk = "object.pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.object.pk
        context["pk"] = con
        return context


@user_passes_test(is_library_admin)
def add_mp3(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddMp3Form(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.library_id = pk
            media.save()
            return redirect("library:media_mp3", pk=pk)
    form = AddMp3Form()
    context = {"form": form, "pk": pk, "library": Library.objects.get(id=pk)}
    return render(request, "media/add_mp3.html", context)


@user_passes_test(is_library_admin)
def add_video(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddVideoForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.library_id = pk
            media.save()
            return redirect("library:media_video", pk=pk)
    form = AddVideoForm()
    context = {"form": form, "pk": pk, "library": Library.objects.get(id=pk)}
    return render(request, "media/add_video.html", context)


@user_passes_test(is_library_admin)
def DeleteMedia(request, id):

    object = get_object_or_404(Media, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:media", pk=object.library_id)


# @user_passes_test(is_library_admin)
def plan(request, pk):
    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    context = {
        "pk": pk,
        "premium": "premium",
        "gold": "gold",
        "basic": "basic",
        "library": library,
    }
    return render(request, "plans/plan.html", context)


# @user_passes_test(is_library_admin)
def process_subscription(request, plan, pk):

    PAYPAL_RECEIVER_EMAIL = "vrepublics@gmail.com"
    # subscription_plan = request.session.get('subscription_plan')
    host = request.get_host()

    # basic_plan = request.POST.get("basic",None)
    # premium_plan = request.POST.get("premium",None)
    # gold_plan = request.POST.get("gold",None)
    # print(premium_plan,gold_plan)
    print(plan)

    # if basic_plan:
    #     price = "10"
    #     billing_cycle = 1
    #     billing_cycle_unit = "M"
    if plan == "basic":
        price = "12"
        billing_cycle = 1
        billing_cycle_unit = "M"
    if plan == "premium":
        price = "30"
        billing_cycle = 1
        billing_cycle_unit = "Y"
    elif plan == "gold":
        price = "150"
        billing_cycle = 1
        billing_cycle_unit = "M"

    library = get_object_or_404(Library, id=pk, library_admin=request.user)
    uniq_id = library.library_name + plan
    print(uniq_id)
    paypal_dict = {
        "cmd": "_xclick-subscriptions",
        "business": PAYPAL_RECEIVER_EMAIL,
        "a3": price,  # monthly price
        "p3": billing_cycle,  # duration of each unit (depends on unit)
        "t3": billing_cycle_unit,  # duration unit ("M for Month")
        "src": "1",  # make payments recur
        "sra": "1",  # reattempt payment on payment error
        "no_note": "1",  # remove extra notes (optional)
        "item_name": "Jmp subscription",
        "custom": uniq_id,  # custom data, pass something meaningful here
        "currency_code": "USD",
        "notify_url": "http://{}{}".format(host, reverse("paypal-ipn")),
        "return_url": "http://{}{}".format(
            host, reverse("library:plan", kwargs={"pk": pk})
        ),
        # 'cancel_return': 'http://{}{}'.format(host,
        #                                       reverse('payment:canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")

    ctx = {"pk": pk, "form": form, "plan": plan, "price": price}
    return render(request, "plans/process_subscription.html", ctx)


@user_passes_test(is_library_admin)
def event(request, pk):

    pk = pk
    media = Event.objects.filter(library=pk)

    context = {"pk": pk, "event": event, "library": Library.objects.get(id=pk)}
    return render(request, "event/event.html", context)


# class UpdateEvent(LoginRequiredMixin,UpdateView):

#     model = Media
#     template_name = 'media/add_media.html'
#     form_class  = UpdateMedia
#     pk  =   'object.pk'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         con = self.object.pk
#         context["pk"] = con
#         return context


@user_passes_test(is_library_admin)
def add_event(request, pk):
    pk = pk
    if request.method == "POST":
        form = AddMediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.library_id = pk
            media.save()
            return redirect("library:event", pk=pk)
    form = AddMediaForm()
    context = {
        "form": form,
        "pk": pk,
    }
    return render(request, "event/add_event.html", context)


@user_passes_test(is_library_admin)
def DeleteEvent(request, id):

    object = get_object_or_404(Event, id=id)
    object.delete()
    # messages.success(request,f'Deleted successfully')
    return redirect("library:event", pk=object.library_id)
