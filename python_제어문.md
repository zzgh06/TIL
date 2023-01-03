# **Python 제어문**

## **Index** 📑
- [조건문](#조건문)
- [레인지(Range)](#레인지range)
- [반복문](#반복문)
    - [while문](#while문)
    - [for문](#for문)
    - [반복문 제어](#반복문-제어)

### **제어문이란**
    - 파이썬은 기본적으로 위에서분터 아래로 순차적으로 명령을 수행
    - 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행(반복)하는 제어가 필요

### **조건문**
    - 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

    * 기본형식
    1) expression에는 참/거짓에 대한 조건식
      - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
      - 이외의 경우 else 이루 들여쓰기 되어있는 코드 블럭을 실행
        - else는 선택적으로 활용 가능
    
    2) 복수 조건문 : 복수의 조건식을 활용할 경우 elif를 활용
      if <expression>:
        # code block
      elif <expression>:
        # code block
      elif <expression>:
        # code block
      else:
        # code block
    
    3) 중첩 조건문 : 조건문은 다른 조건문에 중첩되어 사용될 수 있음
      if <expression>:
        # code block
        if <expression>:
          # code block
      else:
        # code block 
      


#### **예제1**
```python
a = 10
if a >= 0:
    print('양수')
else:
    print('음수')
print(a)
```

#### **실습 1**
- 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력하시오.
- 이때 num은 input을 통해 사용자로부터 입력을 받으시오.
```python
num = int(input())
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
```

#### **실습 2**
- 다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.
```python
dust = 80
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료')
```

### **레인지(Range)**
    - 숫자의 시퀀스를 나타내기 위해 사용 : range(n=0, m, s=1)
      - 기본형 : range(n)
        - 0부터 n-1까지의 숫자의 시퀀스
    
      - 범위지정 : range(n, m)
        - n부터 m-1까지의 숫자의 시퀀스
      
      - 범위 및 스텝 지정 : range(n, m, s)
        - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
    
    - 변경 불가능하며, 반복 가능함

### **예시**
```python
range(4)
  # range(0, 4)
list(range(4))
  # [0, 1, 2, 3]
type(range(4))
  # <class 'range'>
```

```python
# 0부터 특정 숫자까지
list(range(3))
# [0, 1, 2]
# 숫자의 범위
list(range(1, 5))
# [1, 2, 3, 4]
# step 활용
list(range(1, 5, 2))
# [1, 3]
# 역순
list(range(6, 1, -1))
# [6, 5, 4, 3, 2]
list(range(6, 1, 1))
# []
```

### **반복문**
    특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장
    - While 문 : 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함.
    - for 문 : 반복가능한 객체를 모두 순회하면 종료.
    - 반복제어 : break, continue, for-else

#### **While문**
    - while문은 조건식이 참인 경우 반복적으로 코드를 실행
    - 조건이 참인 경우 들여쓰기 되어있는 코드 블록 실행
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하여 반복적으로 실행
    - while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요

```python
while <expression>:
    # Code block
```

### **for문**
    for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체요소를 모두 순회함
      - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음
      - 순회 가능한 객체 : 컨테이너형(문자열, 리스트, 튜플, range, set, dictionary)
```python
for <변수명> in <iterable>:
  # Code block
```
#### **예제2**
```python
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
# apple
# mango
# banana
```

### **문자열 순회**
- 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오.
```python
chars = input() # hi
    
for char in chars:
    print(char)
    
# h
# i
```

- 사용자가 입력한 문자를 range를 활용하여 한 글자씩 출력하시오.
```python
chars = input() # hi
for idx in range(len(charas)):
    print(chars[idx])
    
# h
# i
```

#### **반복문 제어**
    - break: 반복문을 종료
    - continue: continue 이후의 코드 블록은 수행하지 않고, 다음 반복 수행
    - for-else: 끝까지 반복문을 실행한 이후 else 실행
      - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

#### **break**
- break문을 만나면 반복문은 종료됨
```python
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
# 0
# 1
# 2
```

```python
for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
        break
    print(i)
# 0
# 1
# 0과 1만 필요해!
```

#### **continue**
- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# 1
# 3
# 5
```

#### **for-else**
```python
for char in 'apple':
   if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')
    
# b가 없습니다.
```

```python
for char in 'banana':
    if char == 'b':
        print('b!')
        break
    else:
        print('b가 없습니다.')
    
# b!
```