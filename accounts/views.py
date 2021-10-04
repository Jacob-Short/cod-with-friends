from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from accounts.forms import LoginForm, SignupForm
from accounts.models import Soldier

class RootView(View):
    '''root view when not logged in'''

    def get(self, request):
        template = 'root.html'
        context = {}
        return render(request, template, context)



class IndexView(View):
    '''homepage'''

    def get(self, request):
        template_name = "index.html"
        context = {}
        return render(request, template_name, context)


    def post(self, request):
        ...


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
                return redirect('/homepage/')


class SignUpView(View):
    '''create a new user'''

    def get(self, request):
        template_name = "generic_form.html"
        form = SignupForm()
        return render(request, template_name, {"form": form, "header": "Signup"})

    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Soldier.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            login(request, user)
            return redirect(reverse("homepage"))


def logout_view(request):
    logout(request)
    return redirect('/')




    

