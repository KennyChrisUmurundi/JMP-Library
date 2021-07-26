from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

# Create your views here.


class Login(LoginView):
    template_name = "login.html"


# def login_view(request):
#     if request.method == 'POST':
#         form = forms.loginForm(request.POST)
#         if form.is_valid():
#             # email = form.cleaned_data.get('email')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             print(username)
#             if user is not None:
#                 print('logged on succesfully')
#                 login(request,user)
#             else:
#                 print('bado')
#                 return HttpResponseRedirect(reverse('account:login'))
#             return HttpResponseRedirect(reverse('main:store'))
#             # if user is not None and user.role.role == 'receptionist' and user.role.status == 'active':
#             #     return HttpResponseRedirect(reverse('reception:patientsList'))
#             # return HttpResponseRedirect(reverse('reception:patientsList'))
#         else:
#             print('failed')
#             # messages.danger(self.request,"Username or Password incorrect/please try again")
#         # form = forms.loginForm()
#         # context = {
#         # 'form': form
#         # }
#
#     form = forms.loginForm()
#     context = {
#     'form': form
#     }
#     return render(request,'login.html',context)


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("logged on succesfully")
                login(request, user)
            else:
                print("bado")
                return HttpResponseRedirect(reverse("account:login"))
            login(request, user)
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect("main:home")
    else:
        form = forms.UserRegisterForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main:home")
