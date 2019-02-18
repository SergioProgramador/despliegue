from django.urls import path
from . import views
from .views import RutinasListView, RutinaCreateView, RutinaUpdateView, RutinaDeleteView, RutinaPersonalizadaCreateView, RutinaPer_detalle, RutinaPersonalizadaDeleteView, RutinaPersonalizadaUpdateView

urlpatterns = [
    path('', RutinasListView.as_view(), name="rutina_list"),
    path('ejercicios/<int:rutina_id>/', views.ejercicios, name="ejercicios"),
    path('create/', RutinaCreateView.as_view(), name="createRutina"),
    path('update/<int:pk>/', RutinaUpdateView.as_view(), name="updateRutina"),
    path('delete/<int:pk>/', RutinaDeleteView.as_view(), name="deleteRutina"),
    path('createPer/', RutinaPersonalizadaCreateView.as_view(), name="createRutinaPerso" ),
    path('detalle/', views.RutinaPer_detalle, name="rutinap_detalle"),
    path('delete2/<int:pk>/', RutinaPersonalizadaDeleteView.as_view(), name="deleteRutinaPersonalizada"),
    path('update2/<int:pk>/', RutinaPersonalizadaUpdateView.as_view(), name="updateRutinaPersonalizada"),
]