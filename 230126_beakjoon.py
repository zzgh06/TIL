# 10828 : 스택
# import sys
# n = int(sys.stdin.readline())
# stack = []

# for i in range(n):
#     command = sys.stdin.readline().split()
#     if command[0] == 'push':
#         stack.append(command[1])

#     elif command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop()) # 제거된 요소가 나타남
    
#     elif command[0] == 'size':
#         print(len(stack))
    
#     elif command[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
    
#     elif command[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1]) # 가장 위에 있는 정수(나중에 들어간 정수)

# 10101 : 삼각형 외우기
# a = int(input())
# b = int(input())
# c = int(input())

# if a + b + c == 180:
#     if a == 60 and b == 60 and c == 60:
#         print('Equilateral')
#     elif a == b or a == c or c == b:
#         print('Isosceles')
#     else:
#         print('Scalene')
        
# else:
#     print('Error')

# 2720 : 세탁소 사장 동혁

# t = int(input())

# for i in range(t):
#     c = int(input())
#     moneys = [25, 10, 5, 1] # 거스름돈 단위 리스트 생성
#     change = [] # 단위 별 거스름돈 최소 개수를 저장할 빈리스트 생성

#     for j in moneys:
#         change.append(c // j) # 최소 개수를 구하기 위해 // 몫 연산자 사용
#         c = c % j # 다음 반복문 순회 값에 대한 최소 개수를 구하기 위해 % 나머지 연산자 사용
#     print(*change)

# 1453 : 피시방 알바
# n = int(input())
# customer = list(map(int, input().split()))
# cnt = 0 # 거절당하는 수
# seat = [] # 자리

# for i in range(n): 
#     if customer[i] not in seat: # 손님이 원하는 자리 번호가 seat 리스트 안에 없다면
#         seat.append(customer[i]) # seat 리스트에 추가
#     else:
#         cnt += 1 # 그렇지 않은 경우 cnt 변수에 1씩 추가(거절)

# print(cnt)

# 10773 : 제로
# import sys

# k = int(input())
# total = []

# for i in range(k):
#     n = int(sys.stdin.readline()) 
#     if n == 0: # n의 입력 값이 0일 경우
#         total.pop() # total 리스트에서 제거(최근 수를 제거해야하기 때문에 pop() 활용)
#     else:
#         total.append(n) # 0이 아닐 경우 total 리스트에 그 값을 추가

# print(sum(total))

# 2161 : 카드 1
# n = int(input())
# card = [i for i in range(1, n + 1)] # 1 부터 n 까지 순서대로 나열된 리스트 생성
# dis_card = [] # 버릴 카드를 저장할 빈 리스트 생성

# while len(card) > 1: # card의 요소가 1개가 될때 까지 반복
#     dis_card.append(card.pop(0)) # 제일 위의 카드를 버린다
#     card.append(card.pop(0)) # 제일 위의 카드를 제일 아래에 있는 카드 밑으로 옮긴다

# print(*dis_card, card[0])
