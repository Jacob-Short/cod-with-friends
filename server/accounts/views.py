from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

# models
from accounts.forms import LoginForm, RegisterForm
from accounts.models import Soldier, UserAccount
from accounts.models import UserAccount

# serializsers
from accounts.serializers import UserAccountSerializer

# rest
from rest_framework.viewsets import ModelViewSet
from accounts.serializers import UserAccountSerializer


class RootView(View):
    '''root view when not logged in'''

    def get(self, request):
        template = 'root.html'
        context = {}
        return render(request, template, context)


class LoginView(View):
    '''login user'''

    def get(self, request):
        template_name = "generic_form.html"
        form = LoginForm()
        context = {"form": form, "header": "Login"}
        return render(request, template_name, context)

    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return redirect('/')


class RegisterView(View):
    '''create a new user'''

    def get(self, request):
        template_name = "generic_form.html"
        form = RegisterForm()
        return render(request, template_name, {"form": form, "header": "Signup"})

    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = UserAccount.objects.create_user(
                username=data.get("username"),display_name=data.get("display_name"), password=data.get("password")
            )
            login(request, user)
            return redirect(reverse("/"))


def logout_view(request):
    logout(request)
    return redirect('/')


class ManufacturerViewSet(ModelViewSet):
    '''get all users'''
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()