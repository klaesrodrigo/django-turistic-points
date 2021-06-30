from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import TuristicPoint
from resources.api.serializers import ResourceSerializer
from comments.api.serializers import CommentSearializer
from avaliations.api.serializers import AvaliationSearializer
from addresses.api.serializers import AddressSerializer


class TuristicPointSerializer(ModelSerializer):
    resources = ResourceSerializer(many=True)
    avaliations = AvaliationSearializer(many=True)
    comments = CommentSearializer(many=True)
    address = AddressSerializer()
    complete_description = SerializerMethodField()

    class Meta:
        model = TuristicPoint
        fields = (
            "id",
            "name",
            "description",
            "photo",
            "complete_description",
            "complete_description2",
            "resources",
            "avaliations",
            "comments",
            "address",
        )

    def get_complete_description(self, obj):
        return "%s - %s" % (obj.name, obj.description)
