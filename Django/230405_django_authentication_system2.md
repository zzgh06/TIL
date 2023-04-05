# Django-Authentication System 2

## 회원가입

**회원가입**

    User 객체를 Create 하는 것(create 생성 로직과 동일)

    UserCreationForm() : 회원가입을 위한 built-in *ModelForm*

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ...,
  path('signup/', views.signup, name="signup"),
]

회원 가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 
아닌 기존 유저 모델로 인해 작성된 클래스이기 때문에 그냥 'UserCreationForm'으로
작성할 경우 에러 페이지가 나타남.
그래서 커스텀 유저모델을 사용하려면 forms를 다시 작성해야 함
UserCreationForm, UserChangeForm
>>> 두 form 모두 class Meta:model=User가 등록된 form이기 때문
# accounts/form.py

from django.contrib.auth import get_user_model # 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

# accounts/views.py

from .forms import CustomUserCreationForm 
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 후 로그인까지 진행하려면
            # user = form.save()
            # auth_login(request, user)
            # 해당 코드로 변경 및 수정
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```html
<!-- accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="회원가입">
  </form>
{% endblock content %}
```

## 회원탈퇴

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ...,
  path('delete/', views.delete, name="delete"),
]

# accounts/views.py

def delete(request):
    request.user.delete()
    auth_logout(request) # 탈퇴하면서 유저의 세션 정보도 함께 지우고 싶을 경우 auth_logout(request) 추가
    return redirect('accounts:index')
```
```html
<!-- accounts/index.html -->

<form action="{% url 'accounts:delete' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴">
</form><hr>
```

## 회원정보 수정

**회원정보 수정**

    User 객체를 Update 하는 것

    UserChangeForm() : 회원 가입을 위한 built-in *ModelForm*

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ...,
  path('update/', views.update, name="update"),
]

# accounts/views.py

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```
```html
<h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

**UserChangeForm 사용 시 문제점**

    - 일반 사용자가 접근해서는 안될 정보들(fields)까지 모두 수정이 가능해짐
    - admin 인터페이스에서 사용되는 ModelForm 이기 때문
    - 따라서 CustomUserChangeForm에서 저급 가능한 필드를 조정해야 함

```python
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

## 비밀번호 변경

    PasswordChangeForm() : 비밀번호 변경을 위한 built-in Form

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ...,
  path('password/', views.change_password, name='change_password'),
]

# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import *update_session_auth_hash*

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            *update_session_auth_hash(request, user)* # 암호 변경 시 세션 무효화 방지
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```
```html
<h1>비밀번호 수정</h1>
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="비밀번호 수정">
</form>
```

## 로그인 사용자에 대한 접근 제한

**로그인 사용자에 대해 접근을 제한하는 2가지 방법**
    
    1. is_authenticated(속성)
      - 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성(attributes)
      - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, AnnonymousUser에 대해서는 항상 False

    2. login_required(데코레이션)
      - 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
      - 로그인 하지 않은 사용자의 경우 /accunts/login/ 주소로 redirect 시킴

**is_authenticated 적용하기**
```html

<!-- index.html -->

<!-- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기 -->
  {% if request.user.is_authenticated %} 
    <h1>로그아웃</h1>
    <h3>{{ user }}님 안녕하세요!</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="로그아웃">
    </form><br>
    <a href="{% url 'accounts:update' %}">회원정보수정</a><br>
    <a href="{% url 'accounts:change_password' %}">비밀번호수정</a>
    <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form><hr>
    <h3>username: {{ user.username }}</h3>
    <h3>email: {{ user.email }}</h3>
    <h3>first_name: {{ user.first_name }}</h3>
    <h3>last_name: {{ user.last_name }}</h3>
  {% else %}
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">[로그인]</a>
    <a href="{% url 'accounts:signup' %}">[회원가입]</a>
  {% endif %}
```
```python
# views.py

# 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 처리하기
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

**login_required 적용하기**
```python
# views.py

# 인증된 사용자만 게시글을 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 수정

from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
  pass

@login_required
def delete(request):
  pass

@login_required
def update(request):
  pass

@login_required
def change_password(request):
  pass
```