"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include  # Task 3.5
from rango import views  # Task 3.4

from django.conf import settings  # Task 4.3
from django.conf.urls.static import static  # Task 4.3

urlpatterns = [
    path("", views.index, name="index"),  # Task 3.4
    path("rango/", include("rango.urls")),  # Task 3.5
    # # The above maps any URLs starting with rango/ to be handled by rango.
    path("admin/", admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Task 4.3
