from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

# forms
from accounts.forms import LoginForm, SignupForm

# models
from soldier.models import Soldier
from accounts.models import MyUser, UserAccount

# rest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# serializers
from accounts.serializers import UserAccountSerializer, CreateUserAccountSerializer


class IndexView(APIView):
    """index for client"""

    def get(self, request, format=None):
        ...

    serializer_class = UserAccountSerializer

    def post(self, request, format=None):
        ...


class HomeView(APIView):
    """home for client"""

    def get(self, request, format=None):
        ...

    serializer_class = UserAccountSerializer

    def post(self, request, format=None):
        ...

class LoginView(APIView):
    """login existing user"""

    def get(self, request, format=None):
        ...

    serializer_class = UserAccountSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.first_name
            last_name = serializer.last_name
            picture = serializer.picture
            bio = serializer.bio
            display_name = serializer.display_name

            user = authenticate(
                request,
                username=serializer.get("username"),
                password=serializer.get("password"),
            )
            if user:
                login(request, user)
                return Response(UserAccountSerializer(user).data, status=200)


class RegisterView(APIView):
    """create an account"""

    def get(self, request, format=None):
        ...

    serializer_class = CreateUserAccountSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                password = serializer.password
                username = serializer.username
                first_name = serializer.first_name
                last_name = serializer.last_name
                email = serializer.email
                bio = serializer.bio
                display_name = serializer.display_name
            new_user = MyUser.objects.create(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                bio=bio,
                display_name=display_name,
            )
            if new_user:
                login(request, new_user)
                return Response(CreateUserAccountSerializer(new_user).data, status=200)
        except Exception as err:
            print(err)
            return redirect('/')
