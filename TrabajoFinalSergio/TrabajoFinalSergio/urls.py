"""TrabajoFinalSergio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Paths de centro
    path('', include('centro.urls')),
    # Paths de rutina
    path('rutinas/', include('rutina.urls')),
    #Paths de contacto
    path('contacto/', include('contacto.urls')),
    #Paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    #Paths de registration
    path('accounts/', include('registration.urls')),
    #Paths de inscripcion
    path('inscripcion/', include('inscripcion.urls')),
    #Paths de actividad
    path('actividad/', include('actividad.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
    #Paths del ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Paths del modulo django-tellme
    path('tellme/', include("tellme.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if(settings.DEBUG):
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)