from django.urls import path, include
from .views import Register
from . import views


urlpatterns = [
    path('register/', Register.as_view(), name="register"),

]