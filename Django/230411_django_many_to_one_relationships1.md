# Django-Many to one relationships 

## Comment & Article(모델 관계 설정)

    Many to one relationships - N:1 or 1:N
      - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

    Comment(N) - Article(1)
      - 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다

    ForeignKey()
      - django에서 N:1 관계 설정 모델 필드

**Comment 모델 정의**

```python
# article/models.py

class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
- 작성하는 위치와 상관 없이 필드 마지막에 생성됨
```

**ForeignKey(to, on_delete)**

    - to : 참조하는 모델 class 이름
    - on_delete : 참조하는 모델 class가 삭제 될 때 연결된 하위 객체의 동작을 결정
      "CASCADE" : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제


## Comment & Article(관계 모델 참조)

**역참조**

    - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조
    - N:1 관계에서는 1이 N을 참조하는 상황
    - '하지만 Article에는 Comment를 참조할 어떤한 필드도 없다'

    *article.comment_set.all()*
      - article : 모델 인스턴스
      - comment_set : *related manager
      - all() : QuerySetAPI

**related manager**

    N:1 혹은 M:N 관계에서 역참조 시에 사용하는 manager

    related manager가 필요한 이유
      - article.comment 형식으로는 댓글 객체를 참조 할 수 없음
      - 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
      - 대신 Django가 역참조 할 수 있는 'comment_set'manager를 자동으로 생성해
        article.comment_set 형태로 댓글 객체를 참조할 수 있음
      - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐


## Comment & Article(댓글 기능 구현)

### **Comment CREATE**

```python
1) 사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 작성

# article/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

2) detail 페이지에서 CommentForm 출력

# article/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
     context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

```html
3) detail 페이지에서 CommentForm 출력

<!-- article/detail.html -->

  <form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

```python
# article/urls.py

urlpatterns = [
  ...
  path('<int:article_pk>/comments/', views.comment_create, name="comment_create"),

# article/views.py

def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 False로 지정하면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = **comment_form.save(commit=False)**
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article_pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
]
```
```html
<!-- article/detail.html -->

  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

**save(commit=False)**

    DB에 저장하지 않고 인스턴스만 반환


### **Comment READ**

```python
전체 댓글 출력(view 함수)

# article/views.py
from .models import Article, Comment

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

```html
전체 댓글 출력(템플릿)
<!-- articles/views.py -->

<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
```

### **Comment DELETE**

```python
1) 댓글 삭제 url 작성

# articles/urls.py

app_name = 'articles'
urlpatterns = [
  ...
  path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name="comment_delete"),
]

# 몇 번 댓글을 삭제해야 하는지 (댓글 조회) => 댓글을 조회할 pk를 받아야 함
# 댓글이 삭제된 이후 detail 페이지로 redirect => 몇 번 게시글의 detail?? => 게시글을 조회할 pk도 필요

2) 댓글 삭제 view 함수 작성

# articles/urls.py

def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)

    # 댓글 삭제를 요청하는 자 vs 댓글 작성자
    if request.user == comment.user:
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
3) 댓글 삭제 버튼 작성

<!-- article/detail.html -->

<ul>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
    </li>
  {% endfor %}
</ul>
```

### **참고**

**댓글 개수 출력하기**
```html
DTL filter-length 사용
{{ comments|length }}
{{ article.comment_set_all|length }}
```

**댓글이 없는 경우 대체 컨텐츠 출력**
```html
DTL tag-for empty 사용
{% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
    </li>
{% empty %}
  <p>댓글이 없어요</P>
{% endfor %}
```