# 모듈과 예외처리
## **딕셔너리**
    딕셔너리
    - 키-값(key-value) 쌍으로 이뤄진 모음(collection)
    - 키와 값은 : 로 구분, 개별요소는 , 로 구분
    - 변경, 반복 가능

### 생성
    - key와 value가 쌍으로 이뤄진 자료구조 : movie = {'title' : '설국열차'}
    - key에는 리스트 x, value에만 리스트 사용 가능.

### 키-값 추가 및 변경
    - 딕셔너리에 키와 값의 쌍을 추가할 수 있음
    - 이미 해당하는 키가 있다면 기존 값이 변경
    > students = {'홍길동' : 100, '김철수' : 90}
      students['홍길동'] = 80
      # {'홍길동' : 80, '김철수' : 90}
    > students['박영희'] = 95
      # {'홍길동' : 80, '김철수' : 90, '박영희': 95}
### 키-값 삭제
    - 키를 삭제하고자하면 .pop()을 활용하여 삭제하고자 하는 키를 전달
    > students = {'홍길동': 30, '김철수': 25}
      students.pop('홍길동')
      students
      # {'김철수': 25}

### 딕셔너리 순회
    - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
    > grades = {'john': 80, 'eric': 90}
      for name in grades:
        print(name, grades[name]) 
      # john 80
      # eric 90

    - 추가 메서드를 활용하여 순회할 수 있음
      keys() : key로 구성된 결과
      values() : value로 구성된 결과
      items() : (Key, value)의 튜플로 구성된 결과

    > grades = {'john': 80, 'eric': 90}
      print(grades.keys())    # dict_keys(['john', 'eric'])
      print(grades.values())  # dict_values([80, 90])
      print(grades.items())   # dict_items([('john': 80), ('eric': 90)])

# 모듈

> 모듈 => 패키지 => 라이브러리
- pip : 관리하는 관리자
- 다양한 파일을 하나의 폴더를 ***모듈***이고 이러한 폴더들이 모여 ***패키지***를 이루고 다양한 패키지를 하나의 묶음이 
***라이브러리***이다. 

## 모듈 활용하기

- 로또 번호 생성기
```python
# 1. 모듈 가져오기
import random
random_numbers = random.sample(range(1,46),6) # [28, 11, 17, 44, 43, 35]
# 정렬하기
print(sorted(random.sample(range(1,46),6))) # [11, 17, 28, 35, 43, 44]
```

### .sort()와 sorted()의 차이?
     .sort()는 매서드
    - 매서드의 return은 None
    - 해당 리스트 자체를 정렬하지만 반환값은 없음

    - sorted() 는 함수
    - 정렬된 리스트를 반환

```py
numbers = [5,1,2]
result = numbers.sort()
print(numbers) # [1,2,5] / 리스트 자체를 정렬
print(result) # None / 반환값은 없다
numbers = [6,1,2]
result = sorted(numbers)
print(result) # [1,2,6] / 정렬된 리스트를 반환함
```

# 에러/예외 처리

## 디버깅 방법
    - branches: 모든 조건이 원하는대로 동작하는가?
    - for loops: 반복문에 진입하는가? 원하는 횟수만큼 실행하는가?
    - while loops: 반복문에 진입하는가? 원하는 횟수만큼 실행하는가? 종료 조건이 제대로 동작하는가?
    - function: 함수 호출, 함수 파라미터, 함수 결과 확인


## 에러
### 문법에러(Syntax Error)
     캐럿기호(^)로 문법 에러난 가장 앞의 위치를 알려준다.

    - EOL(end of line): 괄호나 따옴표 등이 닫히지 않은 상태
    - EOF(end of File): 실행 중에 ctrl-d에 의해 갑자기 종료 되었을때 
    - Invalid syntax: ':' 누락
    - assign to literal: 예약어 등 변수명으로 짓을 수 없을때

### 예외
    - 문법적으로 올바르더라도 발생하는 에러
    - 여러 타입으로 나타나고, 타입의 메시지의 일부로 출력됨.
    - 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
    - 사용자 정의 예외를 만들어 관리할 수 있음

### 예외의 종류
    - ZeroDivisionError: 0으로 나눌때
    - NameError: 선언되지 않은 변수를 참조할때
    - TypeError: 타입 불일치 / arguments 부족
    - IndexError: (반복할때) 마지막 인덱스보다 초과 순회할때
    - keyError: 없는 key를 호출할때
    - ValueError: 타입은 올바르나 값이 적절하지 않거나 없는 경우
    - ModuleNotFoundError: 없는 모듈을 불러올떄
    - ImportError: Module은 있으나 존재하지 않는 클래스/함수를 가져올때
    - IndentationError: Indentation이 적절하지 않는 경우
    - keyboardInterrupt: 임의로 프로그램 종료할때

  ```python
  10/0 # ZeroDivisionError
  print(name_error) # NameError
  1 + '1' # 타입 불일치
  random.sample() # 인자를 넣지 않았기 때문에 TypeError
  ```

### 예외처리
    - try/except 절
      - try문
        - 오류가 발생할 가능성이 있는 코드 실행
        - 예외가 발생하지 않으면, except절에 가지 않고 실행 종료
      - except문
        - try절에서 예외 발생하면, except절이 실행
        - 예외를 적절하게 처리함