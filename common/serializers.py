from rest_framework import serializers
from rest_framework.status import HTTP_200_OK

__all__ = [
    "OnlyValidationSerializer",
    "RequestSerializerMixin",
    "ResponseSerializerMixin",
    "ErrorSerializer",
]


class OnlyValidationSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class RequestSerializerMixin:
    pass


class ResponseSerializerMixin:
    def to_response(self: serializers.Serializer, status: int = HTTP_200_OK):
        return {
            'error_code': status,
            'data': self.data
        }


class ErrorSerializer(OnlyValidationSerializer, ResponseSerializerMixin):
    code = serializers.IntegerField(help_text="오류 코드 - HTTP Status Code")
    message = serializers.CharField(help_text="오류 메세지")
