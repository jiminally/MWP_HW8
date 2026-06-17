import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# 본인 장고 관리자 아이디로 변경!
user = User.objects.get(username='jimin')
token, created = Token.objects.get_or_create(user=user)
print(f"토큰: {token.key}")