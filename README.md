# my-first-django-app

### Environment of Implementation
```bash
conda create -n "env name" python==3.12.4
```
### Install Dependencies
```bash
# pip 최신화
python -m pip install --upgrade pip
# Django 5.1 설치
pip install django==5.1
# Tag 달기 기능에 필요한 패키지
pip install django-taggit
pip install django-taggit-templatetags2
# Form을 장식하는 패키지
pip install django-widget-tweaks
# 이미지 처리에 필요한 패키지
pip install Pillow
```

### Runserver
다운로드 받은 폴더 경로에서 cmd실행후 아래 명령어 실행
```bash
# 마이그레이션 파일 생성
python manage.py makemigrations
# 마이그레이션 적용
python manage.py migrate
# 슈퍼유저 생성
python manage.py createsuperuser
# 로컬서버 실행
python manage.py runserver
```
