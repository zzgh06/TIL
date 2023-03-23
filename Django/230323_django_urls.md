# django - django URLs

## 변수와 URL

**Variable Routing**

    템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해하는 상황에서 "Variable Routing : URL 일부에 벼누를 포함시키는 것"을 활용

**Variable Routing 작성법**

```python
path('articles/<int:num>/', views.hello)
path('hello/<str:name>/', views.greeting)
# Path converters : URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)
```

## APP의 URL

**APP URL mapping**
    각 앱에 URL을 정의하는 것
    프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소 관리를 편하기 하기 위함

```python
# 2번째 앱 생성 후 URL 주소가 겹친다면

from articles import views as articles_views
from pages import views as pages_views

urlpatterns = [
  ...,
  path('pages-index', pages_views.index),
]

# 위와 같은 방법보다 > "URL을 각자 app에서 관리하자"
```

**include()**

    다른 URL들을 참조할 수 있도록 돕는 함수
    (URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URL로 전달)

```python
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('articles/', include('articles.urls')),
  path('pages/', include('pages.urls')),
]
```

## URL 이름 지정

기존 'articles/' 주소가 'articles/index/'로 변경됨

```python
# firstpjt/urls.py

path('articles/', include('articles.urls'))

# articles/urls.py

path('index/', views.index, name='index')

# 기존에 articles/ 주소를 사용했던 모든 위치를 찾아 변경해야 함
```

**Naming URL patterns**

    URL에 이름을 지정하는 것(path 함수의 name 인자를 정의해서 사용)

```python
from django.urls import path
from . import views

urlpatterns = [
  path('index/', views.index, name='index'),
  path('dinner/', views.dinner, name='dinner'),
  path('search/', views.search, name='search'),
]
```

**'url' tag**
    
    주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 변환

```python
{% url 'url-name' arg1 arg2 %}
```

**URL 표기 변화**
```python
{% extends 'base.html' %}

{% block style %}
  <style>
    h1 { 
      color: crimson;
    }
  </style>
{% endblock style %}

{% block content %}
  <h1>Hello, {{ name }}!!</h1>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:search' %}">search</a>
{% endblock content %}
```

## URL Namespace

**URL 이름 지정 후 남은 문제**

```python
articles 앱의 url 이름과 pages 앱의 url 이름이 같아, 단순히 이름만으로는 분리가 어려운 상황

# articles/urls.py

path('index/', views.index, name='index')

# pages/urls.py

path('index/', views.index, name='index')
```

**app_name 속성 지정**

```python
url 이름 + app 이름표 붙이기
# articles/urls.py

app_name = 'articles'
urlpatterns = [
  ...,
]

# pages/urls.py

app_name = 'pages'
urlpatterns = [
  ...,
]
```

**URL tag의 변화**
```python
{% url 'index' %}  >>>  {% url 'articles:index' %}
```
