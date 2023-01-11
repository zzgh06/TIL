# **사용자 정의 클래스**
## **객체 지향 프로그래밍**
    - 객체지향 프로그래밍 이란?
      - 프로그램을 여러 갸의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

    - 객체(object)의 특징
      - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
      - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
      - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

    - 객체지향의 장점
      - 프로그램을 유연하고 변경이 용이
      - 소프트웨어 개발과 보수가 간편, 직관적인 코드 분석

## **클래스와 인스턴스**
 - 객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성
```python
class MyClass: # 클래스 정의
    pass
my_instance = MyClass() # 인스턴스 생성
my_instance.my_method() # 메서드 호출
my_instance.my_attribute # 속성
```

 - 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
 ```python
  Class Person:
    def __init__(self, name):
      self.name = name
  person1 = Person('지민')
  person.name # '지민'
 ```

  - 메소드 : 특정 데이터 차입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
```python
Class Person:
  def talk(self):
    print('안녕')
  def eat(self, food):
    print(f' {food}를 냠냠')

person1 = Peraon()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨를 냠냠
```

### 객체 비교하기
    - ==
      - 동등한(equal)
      - 변수가 참조하는 객체가 동등한 경우(True)
      - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
    
    - is
      - 동일한(identical)
      - 두 변수가 동일한 객체를 가리키는 경우 True
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b) 
# True, False 
# is의 동일한 경우 True를 출력하나 사실상 a와 b는 id 값이 다르기 때문에 Flase가 출력됨

a = [1, 2, 3]
b = a
print(a == b, a is b)
# True True
# b = a 와 같이 해줄때 id 값이 동일해져 True True가 출력됨
```

## **인스턴스**
    - 인스턴스 변수
      - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
      - 각 인스턴스들의 고유한 변수
    - 생성자 메소드에서 self.<name>으로 정의
    - 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당
```python
Class Person:
  def __init__(self, name):
    self.name = name # 인스턴스 변수 정의

john = Person('jhon')
print(john.name) # 인스턴스 변수 접근 및 할당
# jhon
john.name = 'Jhon Kim' # 인스턴스 변수 접근 및 할당
print(jhon.name) # Jhon Kim
```

### **인스턴스 메소드**
    - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
    - 클래스 내부에 저의되는 메소드의 기본
    - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨
```python
Class MyClass
  def instance_method(self, arg1, ...)
```
    - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
      - 매개변수 이름으로 self를 첫번째 인자로 정의
      - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙


    - 생성자(constructor) 메소드
      - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
      - 인스턴스 변수들의 초기값을 설정
        - 인스턴스 생성
        - __init__메소드 자동 호출
```python
Class Person:
  def __init__(self):
    print('인스턴스가 생성되었습니다')
person1 = Person() # 인스턴스가 생성되었습니다.

Class Person:
  def __init__(self, name):
    print(f'인스턴스가 생성되었습니다. {name}' )
person1 = Person('지민') # 인스턴스가 생성되었습니다. 지민
```

    - 소멸자(destructor) 메소드
      - 인스턴스 객체자 소멸(파괴)되기 직전에 호출되는 메소드
```python
Class Person:
  def __del__(self):
    print('인스턴스가 사라졌습니다.')
person1 = Person()
del person1 # 인스턴스가 사라졌습니다.
```

    - 매직 메소드
      - Double underscore(__)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드
      - 특정 상황에 자동으로 불리는 메소드
    - 예시
      - __str__(self), __len__(self), __repr__(self)
      - __lt__(self, other), __le__(self, other), __eq__(self, other)
      - __gt__(self, other), __ge__(self, other), __lne__(self, other)

    - 매직 메소드 예시
      - 객체의 특수 조작 행위를 지정(함수, 연산자 등)
        - __str__ : 해당 객체의 출력 형태를 지정
          - 프린트 함수를 호출할 때, 자동으로 호출
          - 어떤 인스턴스를 출력하면 __str__의 return 값이 출력

        - __gt__ : 부등호 연산자(>. greater than)
```python
Class Circle:
  def __init__(self, r):
    self.r = r

  def area(self):
    return 3.14 * self.r * self.r

  def __str__(self):
    return f' [원] radius : {self.r}'

  def __gt__(self, other):
    return self.r > other.r

c1 = Circle(10)
c2 = Circle(1) 
print(cl) # [원] radius: 10
print(c2) # [원] radius: 1
c1 > c2 # True
c1 < c2 # False
```