# 2563 : 색종이
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다
# 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성

# import sys
# input = sys.stdin.readline

# n = int(input()) # 색종이의 수
# matrix = [[0] * 101 for _ in range(101)] # 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지

# for _ in range(n):
#     x, y = map(int, input().split())
#     for i in range(x, x+10): # 가로, 세로의 크기가 각각 10인 정사각형임으로 x값 기준으로 x+10하여 범위를 설정해준다
#         for j in range(y, y+10): # y값 기준으로 y+10하여 범위를 설정
#             matrix[i][j] = 1 # 2차원 리스트 각 인덱스 좌표 값을 1로 지정

# result = 0 # 넓이를 구하기 위한 변수

# for a in matrix: # matrix를 순회하며
#     result += a.count(1) # 카운트 메서드를 활용하여 1의 개수를 result 변수에 더하여 대입(sum 함수 활용가능)

# print(result)


# 2587 : 대표값 2
# 다섯개의 자연수가 주어질때, 이들의 평균과 중앙값울 구하시오

# numbers = [] # 자연수를 담을 빈 리스트 생성
# for _ in range(5):
#     numbers.append(int(input()))

# num = sorted(numbers) # 중앙값을 구하기 위해 sorted 함수를 통해 리스트 정렬

# print(sum(num)//5)
# print(num[2])


# 25305 : 커트라인
# n, k = map(int, input().split())
# x = list(map(int, input().split()))

# cut = sorted(x) # 입력 받은 x 값을 정렬시킨 후 cut 변수에 대입
# cut.reverse() # 이를 다시 역순으로 뒤집은 후

# print(cut[k-1]) # k-1 인덱스 값을 출력(인덱스는 0부터)

# # reversed() 함수는 '이터레이터' 형식의 값을 리턴해주기 때문에 객체의 주소가 리턴됨, 이를 다시 리스트로 형변환 하기 위하여 list()함수를 사용.
# # reverse()는 원본을 자체를 수정


# 2164 : 카드 2 # 선입선출의 형태 # 시간복잡도에 의해 deque 활용 : (스택과 큐의 기능을 동시에 사용가능)
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
# 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# from collections import deque

# n = int(input())
# card = deque([i for i in range(1, n+1)])  # 카드는 차례로 1부터 N까지

# while len(card) != 1:
#     card.popleft()  # 제일 위에 있는 카드를 바닥에 버린다
#     temp = card.popleft()  # 제일 위에 카드가 제거된 후 그 다음 제일 위에 위치한 카드를 변수(temp)로 저장
#     card.append(temp) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
#     # 다른 방법 1) card.append(card.popleft()) 와 같이 따로 변수처리하지 않고 바로 append에 넣어도 된다
#     # 다른 방법 2) card.rotate(-1) # 첫번째 원소를 popleft()를 이용해 제거를 하고 두번쨰 원소를 저장하고 다시 append할 필요 없이 rotate함수를 이용해 맨 뒷자리로 위치시키면 된다.

# print(card[0])

# deque 사용법
# 1) from collections import deque
# 2) deque 생성 : dq = deque()
# 3) append() : deque 뒤(오른쪽)에 값 추가 
# 4) appendleft() : deque 앞(왼쪽)에 값 추가 
# 5) extend() : deque 뒤(오른쪽)에 iterable 객체를 순환하며 값들을 차례로 추가
# 6) remove() : deque 안의 특정 값 삭제 
# 7) pop() : deque 뒤(오른쪽)의 값 삭제 후 반환
# 8) popleft() : deque 앞(왼쪽)의 값 삭제 후 반환
# 9) rotate() : deque 안의 값들 회전(함수의 인자로 전달한 값만큼 회전하며 음수를 전달하면 거꾸로 회전)