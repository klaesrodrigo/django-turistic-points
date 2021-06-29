from rest_framework.serializers import ModelSerializer
from avaliations.models import Avaliation


class AvaliationSearializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = ("id", "user", "comment", "note")
