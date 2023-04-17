# Django - Many to many relationships 1

## **ManyToManyFiled**

**ManyToManyFiled**

    ManyToManyFile(to, **options)
      - many-to-many 관계 설정 시 사용하는 모델 필드
      - 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
          - add(), remove(), create(), clear() 등


    ManyToManyField's Arguments
      1. related_name
        - 역참조시 사용하는 manager name을 변경
      
      2. through
        - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여
          중개 테이블을 나타내는 Django 모델을 지정
        - 일반적으로 중개테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는
          경우에 사용됨.
      
      3. symmetrical
        - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
        - 기본 값 : True
        - True일 경우
          - _set 매니저를 추가하지 않음.
          - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로
            target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
          - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨(팔로우, 팔로잉)
        
        - 대칭을 원하지 않는 경우 False로 설정

## **Article & User**

**Many to many relationships**

    N:M or M:N
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우 양쪽 모두에서 N:1 관계를 가짐

    Article(M) - User(N)
    - 0개 이상의 게시글은 0명 이상의 회원과 관련된다.
    - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

**모델 관계 설정**

```python
1) ManyToManyField 작성

# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

2) 모델 작성 후 Migration 진행하면 에러발생
(이유)
like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성되는데 이전의 N:1(Article-User)관계에서 이미 해당 매니저응 사용 중이여서 중복되어 구분이 어려워짐.
그래서 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name를 작성해야 함.

3) related_name 작성 후 migration

# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, *related_name='like_articles'*)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**User-Article간 사용 가능한 related manager 정리**

    - article.user
      게시글을 작성한 유저 - N:1
    
    - user.article_set
      유저가 작성한 게시글(역참조) - N:1

    - article.like_users
      게시글을 좋아요한 유저 - M:N

    - user.like_articles
      유저가 좋아요한 게시글(역참조) - M:N

**좋아요 구현**

```python
1) url 및 view 함수 작성

# articles/urls.py

app_name = 'articles'
urlpatterns = [
  ...
  path('<int:article_pk>/likes/', views.likes, name='likes'),
]

# articles/views.py

@login_required
def likes(request, article_pk):
    # 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)
    # 좋아요 관계를 추가 or 삭제
    # case1. 현재 좋아요를 요청하는 유저가 해당 게시글의 좋아요를 누른 유저 목록에 있는지 없는지를 확인
    if request.user in article.like_users.all():
    # case2. 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회
    # if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article)
    return redirect('articles:index')
```
```html
2) index 템플릿에서 각 게시글에 좋아요 버튼 출력

<!-- articles/index.html -->

{% for article in articles %}
    ...
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소">
      {% else %}
        <input type="submit" value="좋아요">
      {% endif %}
    </form>
    <hr>
  {% endfor %}
```

## **참고**

    .exists()
    QuerySet 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환 특히 큰 QuerySet에 있는 특정 객체의 존재와 관련된 검색에 유용
