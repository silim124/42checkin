from urllib.parse import urlencode
import requests

from common.api_excpetions import InvalidCredentialError
from core import settings


__all__ = [
    "CadetLoginHelper"
]


class CadetLoginHelper:
    @classmethod
    def request_access_token(cls, code: str) -> str:
        base_url = "https://api.intra.42.fr/oauth/token"
        query_dict = {
            "client_id": getattr(settings, "CLIENT_ID"),
            "redirect_uri": getattr(settings, "CALLBACK_URI"),
            "client_secret": getattr(settings, "CLIENT_SECRET"),
            "response_type": "code",
            "code": code,
            "grant_type": "authorization_code",
            "scope": "public",
        }
        token_response = requests.post(f"{base_url}?{urlencode(query_dict)}").json()
        print(token_response)
        if 'error' in token_response:
            raise InvalidCredentialError(detail="토큰 값을 얻어올 수 없습니다.")
        return token_response.get("access_token")

    @classmethod
    def fetch_cadet_name(cls, token: str) -> str:
        header = "Bearer " + token
        base_url = "https://api.intra.42.fr/v2/me"
        cadet_response = requests.get(base_url, headers={"Authorization": header}).json()
        if 'error' in cadet_response:
            raise InvalidCredentialError(detail="해당 프로필이 존재하지 않습니다.")
        if cadet_response['staff?']:
            raise InvalidCredentialError(detail="카뎃만 로그인 할수 있습니다.")
        return cadet_response['login']
