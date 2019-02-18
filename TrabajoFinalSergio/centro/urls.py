from django.urls import path
from . import views
from .views import CentroCreateView, CentroUpdateView, CentroDeleteView

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', CentroCreateView.as_view(), name="createCentro"),
    path('update/<int:pk>/', CentroUpdateView.as_view(), name="updateCentro"),
    path('delete/<int:pk>/', CentroDeleteView.as_view(), name="deleteCentro"),
]