"""api_points URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers

from addresses.api.viewsets import AddressViewSet
from avaliations.api.viewsets import AvaliationViewSet
from core.api.viewsets import TuristicPointViewSet
from resources.api.viewsets import ResourceViewSet

router = routers.DefaultRouter()
router.register("addresses", AddressViewSet)
router.register("avaliations", AvaliationViewSet)
router.register("resources", ResourceViewSet)
router.register("turistic-points", TuristicPointViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
