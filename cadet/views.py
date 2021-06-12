import logging
from urllib.parse import urlencode
from django.shortcuts import redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from core import settings
from cadet.serializers import CadetLogInRequestSerializer, CadetLogInResponseSerializer
from common.serializers import ErrorSerializer

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
        new_query = urlencode(query_dict)
        return redirect(f"{base_url}?{new_query}")


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
    def post(self, request: Request) -> Response:
        query_serializer = CadetLogInRequestSerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)
        access_token = query_serializer.validated_data.data["token"]
        logging.debug(f'42 api access token : {access_token}')
        # TODO: access token 받아오기

        # TODO: 토큰 등록 및 cadet user 생성

        response_serializer = CadetLogInResponseSerializer
        return response_serializer.to_response(status=status.HTTP_200_OK)
