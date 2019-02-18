from django.urls import path
from .views import InscripcionCreate, InscripcionHomeView, Inscripcion_detalle, InscripcionUpdate, InscripcionDelete
from . import views

urlpatterns=[
    path('', InscripcionHomeView.as_view(), name="inscripcion_home"),
    path('create/', InscripcionCreate.as_view(), name="create"),
    path('detalle/', views.Inscripcion_detalle, name="inscripcion_detalle"),
    path('update/<int:pk>/', InscripcionUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', InscripcionDelete.as_view(), name="delete"),
]