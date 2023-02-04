# **사용자 정의함수**
**함수 기본 구조**

    - 선언과 호출(define & call)
    - 입력(Input)
    - 범위(Scope)
    - 결과값(Output)

**선언과 호출**

    - 함수의 선언은 def 키워드를 활용
    - 들여쓰기를 통해 Fonction body(실행될 코드 블록)를 작성
    - 함수는 parameter를 넘겨줄 수 있음
    - 동작 후에 return을 통해 결과값을 전달
    - 함수는 함수명()으로 호출

**함수의 결과값(output)**

    return
    - 함수는 반드시 값을 하나만 return한다
        - 명시적인 return이 없는 경우에도 None을 반환한다.
    - 함수는 return과 동시에 실행이 종료
    - return은 두개 이상 줄 수 없으며, 두 개 이상을 반환하기 위해서는 튜플 형태로 작성 한다.

```python
def minus_and_product(x, y):
  return x - y, x * y
minus_and_product(4,5) # 결과 (-1, 20)
```

**함수의 입력(Input)**

    parameter VS argument
    - Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
    - Argument : 함수를 호출 할 때, 넣어주는 값
      - positional arguments : 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
        ex) def add(x, y):      add(2, 3)
                return x + y
      - keyword arguments : 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
        ex) def add(x, y):      add(x=2, y=5)
                return x + y    add(2, y=5)
      - Default Argument Values : 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
        ex) def add(x, y=0):  add(2)
                return x + y
      - 정해지지 않은 개수의 arguments 는 parameter에 *를 붙여 표현
      - 정해지지 않은 개수의 keyword arguments에 **를 붙여 표현

```python
def function(ham): # parameter : ham
  return ham
function('spam') # argument : 'spam'
```

**함수의 범위(Scope)**

    - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
    - scope
      - global scope : 코드 어디에서든 참조할 수 있는 공간
      - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능

    - variable
      - global variable : global scope에 정의된 변수
      - local variable : local scope에 정의된 변수

    - 객체 수명주기
     - built-in scope : 파이썬이 실행된 이후부터 영원히 유지
     - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
     - local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

    - 이름 검색 규칙
    - 파이썬에서 사용되는 이름(식별자)들은 이름공간에 저장되어 있음
    - 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
     - Local scope : 함수
     - Enclosed scope : 특정 함수의 상위 함수
     - Global scope : 함수 밖의 변수, Import 모듈
     - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
    - 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음


