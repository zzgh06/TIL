# 230204 individual learning : 리스트 함수, 리스트 내포

## **리스트 함수**
    enumerate()
    - 인덱스와 원소로 이루어진 튜플 생성
    - 기본 형태 'for 인덱스, 값 in enumerate(리스트)'

```python
fruits = ['바나나', '사과', '포도']
a = enumerate(fruits)
print(list(a)) # [(0, '바나나'), (1, '사과'), (2, '포도')]

for i, fruit in enumerate(fruits)
  print(i, fruit) 
# 0 바나나
# 1 사과
# 2 포도
```

    ''.join()
    - 문자열로 된 리스트를 합쳐서 반환해주는 함수

```python
"".join(['A', 'B', 'C']) # ABC
" ".join(['A', 'B', 'C']) # A B C
",".join(['A', 'B', 'C']) # A,B,C
```

## **리스트 내포(list comprehension)**
    반복가능한 것을 기반으로 새로운 리스트를 만들어내는 문법
    기본형태 : [표현식 for 반복문]
    기본형태에 조건문을 추가해서도 사용할 수 있음.
    [표현식 for 반복문 조건문] > [2 * i + 1 for in range(0, 10) if i % 2 = 0]