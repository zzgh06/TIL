# Django - Django rest framework

## REST API

**REST API**

    API
    애플리케이션과 프로그래밍으로 소통하는 방법

    REST(Representational State Transfer)
    - API Server를 개발하기 위한 일종의 소프트웨어 설계방법론

    1. HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시
    2. HTTP Method(POST, GET, PUT, DELETE, PATCH 등)를 통해
    3. 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미.

    자원을 정의하고 주소를 지정하는 방법
    1. 자원의 식별 : URI
    2. 자원의 행위 : HTTP methods
    3. 자원의 표현 : JSON으로 표현된 데이터를 제공

    REST API
    REST라는 API 디자인 아키텍처를 지켜 구현한 API

    REST API는 클라이언트와 서버 간의 통신을 위한 규칙을 정의하며, 
    이를 통해 서버 측의 리소스를 클라이언트가 쉽게 요청하고 조작할 수 있게 된다.

    REST API에서는 모든 자원이 고유한 URI(Uniform Resource Identifier)로 식별. 
    클라이언트는 HTTP 메서드(GET, POST, PUT, DELETE 등)를 사용하여 서버에서 자원을 요청하고, 서버는 그에 대한 응답을 반환.

    REST API는 데이터를 XML, JSON 등과 같은 포맷으로 반환할 수 있으며, 이러한 포맷을 사용하여 데이터를 다른 시스템과 공유할 수 있다. 
    또한, REST API는 상태를 저장하지 않고 요청에 대한 응답만 반환하므로(stateless), 서버의 확장성과 유연성을 높일 수 있다.

    REST API는 간결하고 직관적인 인터페이스를 제공하여 다양한 클라이언트와 서버 사이의 통신을 용이하게 만들어준다. 
    또한, REST API는 HTTP 프로토콜을 기반으로 하기 때문에, HTTP의 장점인 캐싱, 프록시, 브라우저 등과의 상호운용성 등을 활용할 수 있다.


## Response JSON

**Django REST framework(DRF)**

    Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리


## Serialization

**Serialization**

    여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    즉, 어떠한 언어나 환경에서도 '나중에 재구성할 수 있는 포맷으로 변환하는 과정'


## DRF - Single Model

```python
1. ModelSerializer 작성
  - articles/serializers.py 생성

# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
```

**ModelSerializer**

    모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동을 만듬
    1. Model 정보에 맞춰 자동으로 필드를 생성
    2. serializer에 대한 유효성 검사기를 자동으로 생성
    3. create() 및 update()의 기본 구현 메서드가 포함됨


**URL과 HTTP requests methods 설계**

||GET|POST|PUT|DELETE|
|:---:|:---:|:---:|:---:|:---:|
|articles/|전체 글 조회|글 작성|||
|articles/1/|1번 글 조회||1번 글 수정|1번 글 삭제|


**게시글 조회**

```python
GET-List
게시글 데이터 목록 조회하기

# articles/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]

# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
      articles = Article.objects.all()
      serializer = ArticleListSerializer(articles, many=True)
      return Response(serializer.data)
```


**'api_view' decorator**

    - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
    - 기본적으로 GET 메서드만 허용되면 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
    - DRF view 함수에서는 필수로 작성


**DETAIL**
```python
GET - Detail
단일 게시글 데이터 조회하기
1. 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

# articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

2. url 및 view 함수 작성
# articles/urls.py

urlpatterns = [
    ...
    path('articles/<int:article_pk>/', views.article_detail),
]

# articles/views.py

from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```

**POST**

```python
POST
게시글 데이터 생성하기
요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답

# articles/views.py

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

새로운 함수에 작성하기보다 def article_list에서 if문을 활용하여 작성.
```

**raise_exception**

        - is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음.
        - DRF에서 제동하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
        
```python
# articles/views.py

@api_view(['GET', 'POST'])
def article_list(request):
    ...
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**DELETE**

```python
게시글 데이터 삭제하기
요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답

# articles/views.py

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

**PUT**

```python 
게시글 데이터 수정하기
요청에 대한 데이터 수정이 성공했을 경우는 200 Ok 상태 코드 응답

# articles/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    ...
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```