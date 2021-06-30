from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import TuristicPoint
from .serializers import TuristicPointSerializer


class TuristicPointViewSet(ModelViewSet):
    serializer_class = TuristicPointSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ("name", "description")

    def get_queryset(self):
        return TuristicPoint.objects.filter(is_approved=True)
