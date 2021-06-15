from urllib.parse import urlencode

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from common.api_excpetions import InvalidCredentialError
from core import settings
from cadet.serializers import CadetLogInRequestSerializer, CadetLogInResponseSerializer
from common.serializers import ErrorSerializer
from . import models
from .models import CadetUser
from .authentication import CadetLoginHelper

__all__ = [
    "CadetCodeView",
    "CadetLogInView",
]


class CadetCodeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request):
        base_url = "https://api.intra.42.fr/oauth/authorize"
        query_dict = {
            "client_id": getattr(settings, "CLIENT_ID"),
            "redirect_uri": getattr(settings, "CALLBACK_URI"),
            "response_type": "code",
        }
        return redirect(f"{base_url}?{urlencode(query_dict)}")


class CadetLogInView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary="카뎃 로그인",
        operation_description="42 api로 로그인하여 토큰 등록 및 cadet user 생성",
        request_body=CadetLogInRequestSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response("로그인 성공", schema=CadetLogInResponseSerializer),
            status.HTTP_400_BAD_REQUEST: openapi.Response("로그인 요청 인자 오류", schema=ErrorSerializer),
            status.HTTP_401_UNAUTHORIZED: openapi.Response("로그인 실패", schema=ErrorSerializer),
        },
    )
    def get(self, request: Request) -> Response:
        query_serializer = CadetLogInRequestSerializer.from_request(request)
        if query_serializer.is_valid():
            data = query_serializer.validated_data
        else:
            raise InvalidCredentialError(detail="인증 코드가 올바르지 않습니다.")
        access_token = CadetLoginHelper.request_access_token(data["code"])
        cadet_name = CadetLoginHelper.fetch_cadet_name(access_token)
        cadet, is_exist = CadetUser.objects.get_or_create(
            name=cadet_name,
            is_staff=False,
            is_superuser=False,
        )
        if cadet is not None:
            login(request, cadet)
        else:
            raise InvalidCredentialError(detail="로그인에 실패하였습니다.")
        response_serializer = CadetLogInResponseSerializer(cadet)
        return response_serializer.to_response(HTTP_201_CREATED)
