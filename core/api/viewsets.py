from rest_framework.viewsets import ModelViewSet
from core.models import TuristicPoint
from .serializers import TuristicPointSerializer


class TuristicPointViewSet(ModelViewSet):
    serializer_class = TuristicPointSerializer

    def get_queryset(self):
        return TuristicPoint.objects.filter(is_approved=True)
