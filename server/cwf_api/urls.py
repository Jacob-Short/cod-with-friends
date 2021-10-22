from django.conf.urls import include, url

from cwf_api.views import (
    IndexView,
    HomeView,
    LoginView,
    RegisterView,
)

from rest_framework import routers


router = routers.DefaultRouter()
router.register('index', IndexView)
router.register('home', HomeView)
router.register('login', LoginView)
router.register('register', RegisterView)

#  using regex so it will ONLY work at localhost 5000
url_patterns = [
    url(r"^api/", include(router.urls))
]