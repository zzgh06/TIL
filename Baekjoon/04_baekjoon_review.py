# 문제 1 : 평균 점수

# total = 0
# for num in range(5): # 5명의 학생임으로 5번 반복되도록 설정
#     n = int(input()) # 1명씩 순서대로 성적 값을 입력
#     if n < 40: # 입력 값 중 40 미만인 경우
#         n = 40 # n의 값에 40을 대입
#     total += n # n의 input 값을 total 변수에 더해감
# print(total//5) # // 정수 값으로만 나눌 때는 슬래쉬 두 번

# 문제2 : X보다 작은 수
# n, x = map(int, input().split()) # 수열 A에 대한 n 값과 정수 x 값을 입력
# arr = list(map(int, input().split())) # 정수 10개로 이루어진 수열 A를 차례대로 입력

# for i in range(n): # 10번 반복되도록 range 함수에 n 값을 입력
#     if arr[i] < x: # 수열 A에 대한 0번째부터 9번째 정수를 차례대로 정수 x와 비교하여 보다 작은 수만
#         print(arr[i], end=" ") # arr 리스트에 남겨 이를 end=" "를 통해 옆으로 차례대로 나열

# 문제 3 :주사위 세개
# a, b, c = map(int, input().split())

# if a == b == c:
#     print(10000 + a * 1000)
# elif a == b or a == c:
#     print(1000 + a * 100)
# elif b == c:
#     print(1000 + b * 100)
# else:
#     print(max(a, b, c) * 100)

# 문제 4 : 0 = not cute / 1 = cute
# P = int(input())
# cute = 0
# not_cute = 0
# for i in range(P):
#     if int(input()) == 1: # input 값이 1과 동일할 경우 cute 변수에 1씩 더해 대입
#         cute += 1
#     else:
#         not_cute += 1 # 그 외에는 not_cute 변수에 1씩 더해 대입 
# print('Junhee is cute!' if cute > not_cute else 'Junhee is not cute!') # print(참 if 조건 else 거짓)

# 문제 5 : 점수계산

# n = int(input())
# eaxm = list(map(int, input().split())) 
# sum = 0
# total = 0 
# for i in range(10):
#     if eaxm[i] == 1: # eaxm 리스트 0~9번째를 순회하면서 1과 동일할 경우 
#         sum += 1 # 변수 sum에 1을 더하여 대입
#         total += sum # 그리고 변수 sum 값을 다시 total 에 더하여 대입 
#     else: # 1이 아닌 경우
#         sum = 0 # 변수 sum의 값을 0으로 초기화
# print(total)