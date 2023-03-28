# Django-ORM
**ORM**

    객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

## QuerySetAPI

**QuerySetAPI**

    ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화하는데 사용하는 도구(API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리)

**QuerySetAPI 구문**

    Article.objects,all()
    model class / Manager / QuerysetAPI

**QuerySet**

    데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
      - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
    
    DjangoORM을 통해 만들어진 자료형

    단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

## ORM CREATE

**QuerySetAPI 사전준비**

```python
# * 외부 라이브러리 설치 및 설정
$ pip install ipython
$ pip install django-extensions

# setting.py

INSTALLED_APPS = [
  'articles',
  'django_extensions,
  ...,
]

$ pip freeze > requirements.txt

# shell_plus 사용 명령어
python manage.py shell_plus
```

**Django shell**

    django 환경 안에서 실행되는 python shell
    (입력하는 QuerySetAPI 구문이 django 프로젝트에 영향의 미침)
  
**데이터 객체를 만드는(생성하는) 방법**
```python
# QuerySetAPI 중 create() 메서드 활용
Article.objects.create(title='제목', content='내용')
```

## ORM READ

**데이터 조회**

```python
# 전체 데이터 조회 : all() 메서드
Article.objects.all()

# 단일 데이터 조회 : get() 메서드
Article.objects.get(pk=1)

# 특정 조건 데이터 조회 : filter() 메서드
Article.objects.filter(content='django!') 
# content='django!'가 들어간 데이터 조회
```

**QuerySetAPI 명령어**
```python
# 오름차순으로 정렬(pk 기준) # order_by() 메서드 
Todo.objects.order_by('pk')

# 내림차순으로 정렬(priority 기준)
Todo.objects.order_by('-priority')

# pk가 1인 단일 데이터의 아래 필드 조회(pk, content, priority, deadline, created_at)
todo = Todo.objects.get(pk=1)
print(todo.pk, todo.content, todo.priority, todo.deadline, todo.created_at)

# pk 필드가 1인 단일 데이터의 journalist 필드 조회
newspaper = Newspaper.objects.get(pk=1)
print(newspaper.journalist)

# journalist 필드가 Laney Mccullough인 데이터 개수 조회
newspapers = Newspaper.objects.filter(journalist='Laney Mccullough')
count = newspapers.count()
print(count)

# pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
newspapers = Newspaper.objects.order_by('-pk')
for newspaper in newspapers:
    print(newspaper.pk, newspaper.title, newspaper.journalist, newspaper.created_at)

# journalist 필드가 Britney를 포함하는 데이터 개수 조회 # in(__contains)
count = Newspaper.objects.filter(journalist__contains='Britney').count()
print(count)

# journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
count = Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()
print(count)

# created_at 필드가 2000-01-01 이후 데이터 개수 조회 gt, gte(초과, 이상)
newspaper = Newspaper.objects.filter(created_at__date__gt=date(2000, 1, 1))
count = newspaper.count()
print(count)

# 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력 last() 메서드 활용
newspaper = Newspaper.objects.last()
print(f"title : {newspaper.title}\ncontent : {newspaper.content}\njournalist : {newspaper.journalist}")

```

