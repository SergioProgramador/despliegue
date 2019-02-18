from django.urls import path
from .views import ActividadListView, ActividadDetailView, ActividadCreate, ActividadUpdateView, ActividadDeleteView

urlpatterns = [
    path('', ActividadListView.as_view(), name="actividad_list"),
    path('<int:pk>/<slug:slug>', ActividadDetailView.as_view(), name="actividad_detail"),  
    path('create/', ActividadCreate.as_view(), name="createActividad"), 
    path('update/<int:pk>/', ActividadUpdateView.as_view(), name="updateActividad"),
    path('delete/<int:pk>/', ActividadDeleteView.as_view(), name="deleteActividad"),
]