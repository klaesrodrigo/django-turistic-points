from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from addresses.api.viewsets import AddressViewSet
from avaliations.api.viewsets import AvaliationViewSet
from comments.api.viewsets import CommentViewSet
from core.api.viewsets import TuristicPointViewSet
from resources.api.viewsets import ResourceViewSet

router = routers.DefaultRouter()
router.register("addresses", AddressViewSet)
router.register("avaliations", AvaliationViewSet)
router.register("comments", CommentViewSet)
router.register("resources", ResourceViewSet)
router.register("turistic-points", TuristicPointViewSet, basename="TuristicPoint")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
