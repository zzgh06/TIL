# django Model

**django Model**

    DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공

```python
#articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  # 1. (models.Model) : django.db.models 모듈의 Model 이라는 부모 클래스를 상속 받아 작성
  # 2. title, content : 클래스 변수명
  # 3. CharField, TextField : model Field 메서드
  # 4. (max_length=10) : model Field 메서드의 키워드 인자(제약조건 관련 설정)
```

## Migrations

**Migrations**

    - model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법
    
    - Migrations 과정 : model class > makeMigrations > Migration 파일(설계도) > migrate > db.sqlite3

    - Migrations 핵심 명령어
    $ python manage.py makeMigrations : model class를 기반으로 설계도(Migration) 작성
    $ python manage.py migrate : 만들어진 설계도를 DB에 전달하여 반영

    - migrate 후 DB 내에 생성 된 테이블 확인

```python
# 이미 생성된 테이블에 추가 필드를 추가해야 한다면?
# 추가모델 필드 작성
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# ChatField() : 길이의 제한이 있는 문자열을 넣을 때 사용(필드의 최대 길이를 결정하는 max_length는 필수 인자)

# TextField() : 글자의 수가 많을 때 사용

# DateTimeField() : 날짜와 시간을 넣을 때 사용
# DateTimeField의 선택인자 
# auto_now : 데이터가 저장될 때마다 자동으로 현재 날짜 시간을 저장
# auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

# 기존의 클래스 위치에 추가할 필드 변수 작성
# 그 이후 다시 $ python manage.py makeMigrations 명령어 실행
# 이미 기존 테이블이 존재하기 때문에 필드를 추가 할 때 필드의 기본 값 설정이 필요

# 이러한 안내문이 생성됨
# You are trying to add a non-nullable field 'category' to todo without a default; we can't do that (the database needs something to populate existing rows).
# Please select a fix:
# 1) Provide a one-off default now (will be set on all existing rows with a null value for this column) 
# 2) Quit, and let me add a default in models.py
# Select an option:

1번 은 직접 기본 값을 입력하는 방법

2번 은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법

# migrations 과정 종료 후 2번째 migration(설계도) 파일이 생성됨
```

## Admin site

**Automatic admin interface**

    django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공

**admin 계정 생성**

```python
$ python manage.py createsuperuser
# email은 선택사항이기 때문에 입력하지 않고 진행 가능
# 비밀번호 생성 시 보안상 터미널에 출력되지 않으니 무시하고 입력을 이어나가도록 함
```

**admin에 모델 클래스 등록**
```python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```