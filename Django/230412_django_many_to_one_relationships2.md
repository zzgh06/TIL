# Django-many to one relationships2

## Article & User(모델 관계 설정)

**User 외래 키 정의**

```python
# article/models.py

from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**User 모델을 참조하는 2가지 방법**

    get_user_model() : 반환 값 - User Object(객체)
      - models.py 가 아닌 다른 모든 곳에서 참조할 때 사용

    settings.AUTH_USER_MODEL : 반환 값 - 'accounts.User'(문자열)
      - models.py의 모델 필드에서 참조할 때 사용

**Migration 진행**

    1) 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있가 떄문에 데이터가 없이는 새로 추가되는
      외래 키 필드 user_id가 생성되지 않음
    2) 그래서 기본 값을 어떻게 작성할 것인지 선택해야 함
    3) 1을 입력하고 Enter 진행(다음화면에서 직접 기본 값 입력)
    4) article으 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
    5) 마찬가지로 1 입력
    6) 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리
    7) migrations 파일 생성 후 migrate 진행


## Article & User(CRUD 구현)

### Article CREATE
```python 
1) ArticleForm 출력 필드 수정

# articles/forms.py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)

2) 게시글 작성 시 user_id 필드 데이터가 누락되어 에러 발생되기 때문에
   게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

# articles/views.py

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

### Article READ
```html
index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력 및 확인

<!-- articles/index.html -->

  {% for article in articles %}
    <p>작성자: {{ article.user.username }}</p> <!-- username 생략가능 -->
    <p>제목: 
      <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
    </p>
    <p>내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
```

### Article UPDATE
```python
1) 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함

# articles/views.py

@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 수정을 요청하는자 vs 게시글의 작성자 비교
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

```html
2) 해당 게시글의 작성자가 아니라면 수정/삭제 버튼을 출력하지 않도록 함

<!-- articles/detail.html -->
{% if request.user == article.user %}
  <form action="{% url 'articles:delete' article.pk  %}" method="POST">
    {% csrf_token %}
 <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
     <input type="submit" value="삭제">
  </form>
{% endif %}
```

### Article DELETE
```python
삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제 할 수 있도록 함

# articles/views.py

@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')
```

## Comment & User(모델 관계 설정)

**User 외래 키 정의**

```python
# articles/models.py

class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Migration 진행**
    
    이전에 Article 와 User 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운
    컬럼이 추가되어야하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요


## Comment & User(CRUD)

### Comment CREATE

```python
댓글 작성 시 작성자 정보가 함께 작성될 수 있도록 save의 commit 옵션 활요

# articles/views.py

def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 False로 지정하면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False)
        comment.article = article
        *comment.user = request.user*
        comment.save()
        return redirect('articles:detail', article_pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

### Comment READ
```html
detail 템플릿에서 각 댓글의 작성자 출력 및 확인

<!-- articles/detail.html -->

{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
  ...
  </li>
{% endfor %}
```

### Comment DELETE
```python
1) 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제 할 수 있도록 함

# articles/views.py

@login_required
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)

    # 댓글 삭제를 요청하는 자 vs 댓글 작성자
    *if request.user == comment.user:*
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
2) 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함

<!-- articles/detail.html -->

<ul>
  {% for comment in comments %}
    <li>
      {{ comment.user }} - {{ comment.content }}
      *{% if request.user == comment.user %}*
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      *{% endif %}*
    </li>
  {% endfor %}
</ul>
```