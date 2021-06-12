from django.urls import path

from .views import *

app_name = "cadet"
urlpatterns = [
    path("code", CadetCodeView.as_view(), name="code"),
    path("login", CadetLogInView.as_view(), name="login"),
]
