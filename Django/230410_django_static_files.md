# Django - static files

## Static files 제공하기

**경로에 따른 Static file 제공하기**

    1. 기본 경로 : app/static/

    2. 추가 경로 : STATICFILES_DIRS

**기본 경로 Static files 제공하기**

    - articles/static/articles/ 경로에 이미지 파일 배치
  
```html
static tag를 사용해 이미지 파일에 대한 url 제공
<!-- articles/index.html -->
{% load static %}

<img src="{% static 'article/sample-1.png %}" alt="img">
```

**추가 경로 Static files 제공하기**

    - 최상단에 static 폴더 생성
    - STATICFILES_DIRS : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

```python
추가 경로에 이미지 파일 배치

# settings.py

STATICFILES_DIRS = [
  BASE_DIR / 'static',
]
```

```html
<!-- articles/index.html -->

<img src="{% static 'sample-1.png %}" alt="img">
```

## Media Files

    Media Files
    - 사용자가 웹에서 업로드하는 정적파일(user-uploaded)

    ImageFiled()
    - 이미지 업로드에 사용하는 모델 필드
    - 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로 문자열'이 DB에 저장

**미디어 파일을 제공하기 전 준비**

    1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

    2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

**MEDIA_ROOT**

```python
미디어 파일들이 위치하는 디렉토리의 절대 경로
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

**MEDIA_URL**

```python
MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
# settings.py

MEDIA_URL = '/media/'
```

**MEDIA_ROOT와 MEDIA_URL에 대한 url 지정**

```python
# crud/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin', admin.site.urls),
  path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

업로드 된 파일의 URL == settings.MEDIA_URL
위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
```

## 이미지 업로드 및 제공하기

### **1) 이미지 업로드**

**blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 설정**

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**migration 진행**
    
    $ pip install pillow

    $ python manage.py makemigrations
    $ python manage.py migrate

    $ pip freeze > requirements.txt

**form 요소의 enctype 속성 추가**

```html
<!-- articles/create.html -->

  <h1>Create</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

**view 함수에서 업로드 파일에 대한 추가 코드 작성성**

```python
# articles/views.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
    ...
```

### **2) 업로드 이미지 제공하기**

```html
url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음

<!-- articles/detail.html -->

<img src="{{ article.image.url }}" alt="img">

이미지를 업로드 하지 않은 게시물은 detail 템플릿을 출력할 수 없는 문제 해결
이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리

<!-- articles/detail.html -->

{% if article.image %}
  <img src="{{ article.image.url }}" alt="img">
{% endif %}
```

### **3) 업로드 이미지 수정**

```html
수정 페이지 form 요소에 enctype 속성 추가

<!-- articles/update.html -->

<h1>Update</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="UPDATE">
</form>
```

```python
view 함수에서 업로드 파일에 대한 추가 코드 작성

# articles/views.py

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
    ...
```

## 참고

**upload_to argument**

    'upload_to' argument
    - ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정

    1. image = models.ImageField(blank=True, upload_to='images/')

    2. image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
