# Django-Authentication System 1

**Django-Authentication System**

    - 사용자 인증과 관련된 기능을 모아 놓은 시스템
    - 인증과 권한 부여를 함께 제공 및 처리

      - Authentication(인증) : 사용자가 자신이 누구인지 확인하는 것
      - Authorization(권한, 허가) : 인증된 사용자가 수행할 수 있는 작업을 결정, 권한 부여

## Custom User model

**Custom User model로 대체하기**
    django가 기본적으로 제공하는 User model은 내장된 auth 모듈의 User 클래스를 사용

```python
대체하기 1.
# AbstractUser를 상속받는 커스텀 User 클래스 작성
# 기존 User 클래스로 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨

# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass # 나중에 커스텀해야 할 때가 생기면 그때 커스텀하고자하는 코드를 작성

대체하기 2.
# django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 USer 모델로 지정

# settings.py

AUTH_USER_MODEL = 'accounts.User'

대체하기 3.
# 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음.

# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
