# 42checkin
## description
`42checkin`은 42Seoul 체크인 시스템을 drf로 구현했습니다.
`42checkin` implemented the check-in system of 42Seoul (with drf). 

<hr>

## .env

.env 파일은 json 형식으로 된 다음과 같은 정보를 담고 있습니다.

client는 42의 api client를 뜻합니다.

```
{
  "SECRET_KEY": "django-insecure-xxxxxxxxxxxxxxxxxxxxxxxx",
  "CLIENT_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "CLIENT_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "CALLBACK_URI" : "http://localhost:8000/cadet/login"
}
```

<hr>

## Run 42checkin on the Local Server

이전에 한번도 시작한 적이 없다면, 다음과 같은 단계를 따릅니다.

If you have never run `42checkin` before, follow these steps:

```
$ python -m venv env
$ source env/bin/activate
$ pip install poetry
$ poetry install
$ ./run.sh
```

시작한 적이 있다면, 이것을 실행하세요.

or 

```
$ source $(poetry env info --path)/bin/activate
$ ./run.sh
```
<hr>

## Lint with flake8 linter

```
$ flake8
```

<hr>

## ETC
이 앱은 오픈소스입니다.

이슈나 추가할 요소가 있다면, 어느 때든 부담없이 pr해주세요!

이외에 궁금한 점이 있다면 `<silim@student.42seoul.kr>`로 이메일 보내주세요.

this app is open source. 

if you find any issues or something to add, you can make a pull request for the project anytime.

you can contact me at `<silim@student.42seoul.kr>`

<br>
