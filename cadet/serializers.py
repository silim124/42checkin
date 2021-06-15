from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from cadet.models import CadetUser
from common.serializers import RequestSerializerMixin, ResponseSerializerMixin, OnlyValidationSerializer

__all__ = [
    "CadetLogInRequestSerializer",
    "CadetLogInResponseSerializer",
]


class CadetLogInRequestSerializer(OnlyValidationSerializer, RequestSerializerMixin):
    code = serializers.CharField()


class CadetLogInResponseSerializer(serializers.ModelSerializer, ResponseSerializerMixin):
    class Meta:
        model = CadetUser
        fields = (
            "name",
            "is_active",
            "create_time"
        )

        is_active = serializers.SerializerMethodField()

    @swagger_serializer_method(serializers.CharField(help_text="카뎃의 active 여부"))
    def get_is_active(self, obj: CadetUser) -> bool:
        return obj.is_active
