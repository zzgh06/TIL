# **이차원 리스트**

## **Index** 📑
1. [이차원 리스트](#이차원리스트)
2. [입력 받기](#입력받기)
3. [순회](#순회)
4. [전치](#전치)
5. [회전](#회전)


### **이차원리스트**
    이차원 리스트는 '리스트를 원소'로 가지는 리스트
               0  1  2    0  1  2    0  1  2
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                  0          1          2

```python
print(matrix[0])
>>> [1, 2, 3]
print(matrix[1])
>>> [4, 5, 6]
print(matrix[2])
>>> [7, 8, 9]

print(matrix[0][0])
>>> 1
print(matrix[1][2])
>>> 6
print(matrix[2][0])
>>> 7
```

    이차원 리스트는 행렬(matrix)이다
|(0, 0)|(0,1)|0, 2)|
|:---:|:---:|:---:|
|1|2|3|
|4|5|6|
|7|8|9|

특정 값으로 초기화 된 이차원 리스트 만들기

```python
#  100 X 100 행렬
matrix = []

for _ in range(100):
  matrix.append([0] * 100)

# n x m 행렬
n = 4 # 행
m = 3 # 열
matrix = []

for _ in range(n):
  matrix.append([0] * m)

print(matrix)
>>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 리스트 컴프리헨션으로 작성(n x m 행렬)
n = 4 # 행
m = 3 # 열

matrix = [[0] * m for _ in range(n)]

print(matrix)
>>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### **입력받기**

```python
# 1. 행렬의 크기가 미리 주어지는 경우
matrix = []

for _ in range(8)
  line = list(input()) # input 함수가 한 줄을 입력 받기 때문에 열의 크기는 사용되지 않는다
  matrix.append(line)

# 리스트 컴프리헨션
matrix = [list(input() for _ in range(8))]


# 2. 행렬의 크기가 입력으로 주어지는 경우
n, m = map(int, input().split()) # 8 7
matrix = []

for _ in range(n):
  line = list(map(int, input().split()))
  matrix.append(line)

# 리스트 컴프리헨션
n, m = map(int, input().split()) # 8 7

matrix = [list(map(int, input().split())) for _ in range(n)] 
```


### **순회**
```python
# 이중 for문을 이용한 행 우선 순회
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(3): # 행의 길이만큼 범위 지정
  for j in range(4): # 열의 길이만큼 범위 지정
    print(matrix[i][j], end=' ') # 행 우선 순회 임으로 matrix[i][j] 으로 순회(좌표로 생각)
  print()

>>>> 1 2 3 4
>>>> 5 6 7 8
>>>> 9 0 1 2


# 이중 for 문을 이용한 열 우선 순회
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(4): # 열의 길이만큼 범위 지정
  for j in range(3): # 행의 길이만큼 범위 지정
    print(matrix[j][i], end=' ') # 열 우선 순회임으로 matrix[j][i] 으로 순회(좌표로 생각)
  print()

>>>> 1 5 9
>>>> 2 6 0
>>>> 3 7 1
>>>> 4 8 2

# 행 우선 순회를 이용해 이차원 리스트의 최대값, 최소값 구하기
# 최대값
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

max_value = 0

for i in range(3):
  for j in range(4):
    if matrix[i][j] > max_value: # 변수 max_value 보다 matrix[i][j] 좌표 값이 더 클 경우
      max_value = matrix[i][j] # matrix[i][j] 좌표 값을 변수 max_value 에 대입

print(max_value)
>>> 10


# 최솟값
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

min_value = 99999999

for i in range(3):
  for j in range(4):
    if matrix[i][j] < min_value: # 변수 min_value 보다 matrix[i][j] 좌표 값이 더 작을 경우
      min_value = matrix[i][j] # matrix[i][j] 좌표 값을 변수 min_value 에 대입

print(min_value)
>>> -1
```

### **전치**
**전치란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다(종이접기처럼 반으로 접었을 때 만나는 값을 서로 맞바꾼다고 생각하면 됨)**
```python
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)] # 전치 행렬을 담을 이차원 리스트 초기화(행과 열의 크기가 반대)

for i in range(4):
  for j in range(3):
    transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기

"""
transposed_matrix = [
  [1, 5, 9],
  [2, 6, 0],
  [3, 7, 1],
  [4, 8, 2]
]
"""
```


### **회전**
문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.
```python

# 1. 왼쪽으로 90도 회전하기
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    rotated_matrix[i][j] = matrix[j][n-i-1] # 오른쪽 열 위(0, 2) 기준으로 아래로 순차적으로 진행됨

"""
rotated_matrix = [
  [3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]
]
"""


# 2. 오른쪽으로 90도 회전하기
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    rotated_matrix[i][j] = matrix[n-j-1][i] # 왼쪽 열 밑(2, 0)에서부터 위로 순차적으로 진행 
"""
rotated_matrix = [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
"""
```


