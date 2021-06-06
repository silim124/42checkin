from rest_framework import serializers

from common.serializers import ResponseSerializerMixin

__all__ = [
    "CadetLogInRequestSerializer",
    "CadetLogInResponseSerializer",
]


class CadetLogInRequestSerializer(serializers.Serializer):
    token = serializers.CharField()


class CadetLogInResponseSerializer(serializers.Serializer, ResponseSerializerMixin):
    pass
