# Django - Many to many relationships 2

## Profile 구현

1. 자연스러운 follow 흐름을 위한 프로필 페이지 작성
```python
# accounts/urls.py
urlpatterns = [
  ...
  path('profile/<username>/', views.profile, name='profile'),
]
*주의사항*
path('<username>/', views.profile, name='profile') 으로 작성할 경우,
이후에 작성하는 url도 <username>의 영향을 받게되 새로운 url 작성이 안됨
그래서 1. 해당 url을 제일 밑에 작성하거나 2. 'profile/<username>/'으로 앞에 작성해주면 됨.

# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

2. profile 템플릿 작성
```html
<!-- accounts/profile.html -->

<h1>{{ person.username }}의 프로필 페이지</h1>

<h3>{{ person.username }}가 작성한 모든 게시글</h3>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<h3>{{ person.username }}가 작성한 모든 댓글</h3>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
  
<h3>{{ person.username }}가 좋아요를 누른 모든 게시글</h3>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
```

3. Profile 템플릿으로 이동할 수 있는 하이퍼링크 작성
```html
<!-- accounts/index.html -->

<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>

<P>
  작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
</p>
```

## User & User

    User(M) & User(N)
    - 유저는 0명 이상의 다른 유저와 관련된다.
    - 유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉을 할 수 있다

**Follow 구현**

1. ManyToManyField 작성 및 Migration 진행
```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)

self : 자기 자신을 참조
정참조 : followings (반대도 가능)
역참조 : followers (반대도 가능)
symmetrical : ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용, 기본값 : True 이기 때문에 False(대칭을 원하지 않을 때 사용) 로 설정
```

2. url 및 view 함수 작성
```python
# accounts/urls.py

urlpatterns = [
  ...
  path('<int:user_pk>/follow/', views.follow, name='follow'),
]

# accounts/views.py

@login_required
def follow(request, user_pk):
    # 팔로우를 할 대상이 필요
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
    # 나 자신은 팔로우 할 수 없음
    # 팔로우 or 언팔로우
        if person.followers.filter(pk=request.user.pk).exist():
            # 언팔로우
            person.followers.remove(request.user)
        else:
            # 팔로우
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

3. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
```html
<!-- accounts/profile.html -->

<div>
  팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
</div>

{% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  </div>
{% endif %}
```

4. 사용자 팔로우 목록 조회
```html
<!-- accounts/profile.html -->

<h2>팔로잉 목록</h2>
{% for following in person.followings.all %}
  <p>
    <a href="{% url 'accounts:profile' following.username %}">{{ following.username }}</a>
  </p>
{% empty %}
  <p>팔로잉이 없습니다.</p>
{% endfor %}
<hr>
<h2>팔로워 목록</h2>
{% for follower in person.followers.all %}
  <p>
    <a href="{% url 'accounts:profile' follower.username %}">{{ follower.username }}</a>
  </p>
{% empty %}
  <p>팔로워가 없습니다.</p>
{% endfor %}
```