# 문제 1 : 더하기
# 10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.

# T = int(input()) # 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.

# for t in range(T): # 각 테스트 케이스는
#     N = int(input()) # 첫 줄에 자연수의 개수 N(1 ≤ N ≤ 100)이 주어지고
#     total = (sum(map(int, input().split()))) # 각각의 자연수 사이에는 하나씩의 공백이 있으며 이들의 합을 구해라(합을 구하기 위해 sum 함수 사용)
#     print(total)

# 문제 2 : 네 수
# a, b, c, d = map(str, input().split()) # 첫째 줄에 네 자연수 A, B, C, D가 주어진다.
# ab = int(a + b) # A와 B를 붙인 수(문자열로 두 수를 붙이고 정수로 변환하여 변수에 대입한다)
# cd = int(c + d) # 위와 동일
# print(ab + cd)

# 문제 3 : 네 번째 점
# 세 점의 좌표가 한 줄에 하나씩 주어진다.
# x_l = [] # 좌표 x 값을 저장하기 위한 리스트
# y_l = [] # 좌표 y 값을 저장하기 위한 리스트

# for i in range(3): # 좌표가 3개이므로 3번 순회하도록 설정
#     x, y = map(int, input().split()) # 각 x, y의 좌표값을 입력받음
#     x_l.append(x) # 입력받은 x 값을 리스트에 저장
#     y_l.append(y) # 입력받은 y 값을 리스트에 저장

# for i in range(3): # x_l, y_l 리스트를 순회하기 위해 3번 순회하도록 설정
#     if x_l.count(x_l[i]) == 1: # x_l 리스트 안의 요소 중 1개만 있는 경우(count 함수를 통해 리스트 안의 요소 개수를 확인)
#         X = x_l[i] # 그 i번째 요소를 X 변수에 대입
#     elif y_l.count(y_l[i]) == 1: # y_l 리스트 안의 요소 중 1개만 있는 경우
#         Y = y_l[i] # 그 i번째 요소를 Y 변수에 대입
# print(X, Y)

# 문제 4: A + B - 5
# while True: # while문 활용 
#     a, b = map(int, input().split())
#     total = a + b
#     if a == 0 and b == 0: # a와 b의 값이 0일 경우 
#         break # while 문을 종료시킨다.
#     print(total)

# 문제 5 : 더하기 사이클
# n = int(input())
# num = n
# cnt = 0

# while True:
#     a = num // 10 # 몫 : 십의 자리값
#     b = num % 10 # 나머지 : 일의 자리값
#     c = (a + b) % 10 # 나머지 : 십의 자리와 일의 자리를 더한 값(나머지로 했을 때, 결과가 유지됨)
#     num = (b * 10) + c # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수

#     cnt += 1 # 몇 번 돌았는지(싸이클) 확인 하기 위해 cnt 변수 사용
#     if num == n: # 입력 값 n과 num 변수 값이 같아질 때 
#         break # while문을 종료
# print(cnt)