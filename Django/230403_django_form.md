# Django-Form

**Django Form**

    사용자 입력 데이터를 수집하고, 처리 및 유효성 검증을 수행하기 위한 도구

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField()

# articles/views.py
# Form class를 적용한 new 로직

from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- articles/new.html -->
<!-- Form rendering options -->
<h1>New</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }} <!-- 폼에 정의한 subject, content 속성에 해당하는 HTML 코드를 자동으로 생성 -->
  <input type="submit">
</form>
```

## widgets

**widgets**

    - HTML 'input' element의 표현을 담당
    - widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

## Django ModelForm

    - Form : 사용자 입력 데이터를 DB에 저장하지 않을 때(ex. 로그인)
    - ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때(ex. 회원가입)

**ModelForm class 선언**
```python
# articles/form.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta: # ModelForm의 정보를 작성하는 곳 
      model = Article
      fields = '__all__'
```

**fields 및 exclude 속성**
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('title',) # exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
```

**ModelForm을 적용한 create 로직**
```python
# articles/views.py
from .forms import ArticleForm

def create(request):
  form = ArticleForm(request.POST)
  if form.is_valid(): # is_valid() : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
      article = form.save()
      return redirect('articles:detail', article.pk)
  context = {
      'form': form,
  }
  return render(request, 'articles/new.html', context)

# ModelForm 적용 결과 : 제목 : Input에 공백 값을 입력 후 에러 메시지 확인(유효성 검사 결과)
```

**ModelForm을 적용한 edit 로직**
```python
# articles/views.py

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/edit.html', context)
```
```html
<!-- articles/edit.html -->
<h1>Edit</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="[UPDATE]">
</form>
```

**ModelForm을 적용한 update 로직**
```python
# articles/views.py

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save() # 데이터 베이스 객체를 만들고 저장, 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

## 참고
**Widget 응용**
```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )

    # ModeForm의 정보를 작성하는 곳
    class Meta:
        model = Article
        fields = '__all__'
```