# **Python 함수**

## **함수**
우리가 함수를 사용해야 하는 이유
- Abstraction : 복잡한 내용을 숨기고 기능에 집중, 재사용성, 가독성, 생산성
- Decomposition : 기능을 분해, 재사용 가능

```python
numbers = [1, 10, 100]
result = 0
cnt = 0
for number in numbers:
    result += number
    cnt += 1
print(result/cnt)
```
**↓↓↓↓↓↓**
```python
print(sum(numbers)/len(numbers))
```
- psrdev 함수 (파이썬 표준 라이브러리 - statistics)
```python
import statistics
values = [100, 75, 85, 90, 65, 95]
statistics.pstdev(values)
```

**함수의 정의**

    - 특정한 기능을 하는 코드의 조각(묶음)
    - 특정 명령을 수행하는 코드를 필요 시에만 호출하여 간편히 사용
    - 사용자 함수
      - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능
        > def function_name
            # code block
            return returning_value

**함수 기본 구조**

    - 선언과 호출(define & call)
    - 입력(Input)
    - 범위(Scope)
    - 결과값(Output)

**자주 사용하는 함수**

    - len(s)
      객체의 길이를 반환

    - sum(iterable, start=0)
      start 및 iterable 의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 돌려준다

    - max(iterable)
      iterable에서 가장 큰 항목을 반환
    
    - min(iterable)
      iterable에서 가장 wkrdms 항목을 반환
    
**수학 관련 함수**

    - abs(x)
      숫자의 절대값을 반환합니다. 인자는 정수, 실수 또는 __abs__()를 구현하는 객체
    
    - divmod(a, b)
      두 수를 받아 몫과 나머지를 반환

    - pow(base, exp, mod-None)
      base의 exp 거듭제곱을 반환
      mod가 있는 경우, base의 exp 거듭제곱의 모듈로 mod를 반환

    - round(number, ndigit=None)
      number 를 소수점 다음에 ndigits 정밀도로 반올림한 값을 반환
      ndigits 가 생략되거나 None 이면, 입력에 가장 가까운 정수를 반환

**논리 관련 함수**
    - all(iterable)
      iterable의 모든 요소가 참이면(또는 iterable이 비어있으면)True를 반환
    
    - any(iterable)
      iterable의 요소 중 어느 하나라도 참이면 True를 반환
      iterable이 비어 있으면 Flase를 돌려줍니다.

**함수 응용**
    map(function, iterable)
      순회 가능한 데이터구조(iterable)의 모둔 요소에 함수(function) 적용하고, 그 결과를 map object로 반환
      input 값들을 숫자로 바로 활용하고 싶을 때 사용

```python
n, m = map(int, input().split()) # n, m = 3 5
print(n, m) # 3 5 출력됨
```

     
