from drf_yasg import openapi
from drf_yasg.views import get_schema_view


api_doc_view = get_schema_view(
    info=openapi.Info(
        title=f"42checkin API Documentation",
        default_version="v1",
        description="42 체크인 API 문서입니다",
        contact=openapi.Contact(email="silim@student.42seoul.kr"),
    ),
    public=True,
)
