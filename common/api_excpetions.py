from rest_framework import status
from rest_framework.exceptions import APIException

__all__ = [
    "AlreadyAuthenticated",
    "InvalidCredentialError",
]


class AlreadyAuthenticated(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "이미 로그인되어 있습니다."
    default_code = "permission_denied"


class InvalidCredentialError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "로그인에 실패했습니다"
    default_code = "not_authenticated"
