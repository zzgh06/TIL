# django-ORM with view

## 사전준비
**사전준비**

**1. app URLS 분할 및 연결**
```python
# articles/urls.py
from django.urls import path

app_name = 'articles'
urlpatterns = [
]

# crud/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('articles/', include('articles.urls')),
]
```

**2. index 페이지 작성**
```python
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
  path('', views.index, name='index'),
]

# articles/views.py
def index(request):
  return render(request, 'articles/index.html')
```

## READ

**1. 전체게시글 조회**
```python
# articles/views.py
from .models import Article # models에 작성된 Article 클래스를 가져옴

def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)
```

```html
<!-- articles/index.html -->
<h1>Articles</h1>
<hr>
{% for article in articles %} <!-- 전체 게시글이기 때문에 포문 이용 -->
  <P>글 번호: {{ article.pk }}</P>
  <P>글 제목: {{ article.title }}</P>
  <P>글 내용: {{ article.content }}</P>
  <hr>
{% endfor %}
```

**2. 단일 게시글 조회**
```python
# articles/urls.py
urlpatterns = [
  ...,
  path('<int:pk>/', views.detail. name='detail'),
]

# articles/views.py
def detail(request, pk):
  articles = Article.objects.get(pk=pk)
  context = {
    'article' : article, # 전체냐 단일이냐의 따라서 복수 단수 구분하여 작성하면 좋음
  }
  return render(request, 'articles/detail.html', context)
```

```html
<!-- templates/articles/detail.html -->
<h1>Detail</h1>
<h3>{{ article.pk }} 번째 글</h3>
<hr>
<P>제목: {{ article.title }}</P>
<P>내용: {{ article.content }}</P>
<P>작성 시간: {{ article.created_at }}</P>
<P>수정 시간: {{ article.updated_at }}</P>
<hr>
```

## CREATE

    Create 로직을 구현하기 위해 필요한 view 함수 : 2개
    1. 사용자의 입력을 받는 페이지를 렌더링 : new
    2. 사용자가 입력한 데이터를 받아 DB에 저장 : create

**1. new 로직 작성**
```python
# articles/urls.py
urlpatterns = [
  ...,
  path('new/', views.new. name='new'),
]

# articles/views.py
def new(request):
  return render(request, 'articles/new.html')
```

<!-- templates/articles/new.html -->
<h1>New</h1>
  <form action="{% url 'articles:create' %}" method='GET'>
    <div>
      <label for="title">제목: </label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[BACK]</a>
<hr>
```

**2. create 로직 작성**
```python
# articles/urls.py
urlpatterns = [
  ...,
  path('new/', views.new. name='new'),
]

# articles/views.py
def create(request):
  # new에서 보낸 사용자 데이터를 받아서 변수에 할당
  # print(request.GET)
  title = request.GET.get('title')
  content = request.GET.get('content')

  # 저장 전에 유효성 검사와 같은 추가 작업을 위해
  article = Article(title=title, content=content)
  article.save()
  return render(request, 'articles/create.html')
```

```html
<!-- templates/articles/create.html -->
<h1>게시글이 작성되었습니다</h1>
```