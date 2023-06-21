# 최소, 최대
# 문제 : N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# n = int(input())
# array = list(map(int, input().split()))
# print(min(array), max(array))


# 두 수 비교하기
# 문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

# a, b = map(int, input().split())

# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# 시험 성적
# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 출력
# 시험 성적을 출력한다.

# total = int(input())

# if total >= 90:
#     print('A')
# elif total >= 80:
#     print('B')
# elif total >= 70:
#     print('C')
# elif total >= 60:
#     print('D')
# else:
#     print('F')

# 사분면 고르기 
# 문제
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.
# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

# 출력
# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# 합
# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# n = int(input())
# total = 0

# for i in range(1, n+1):
#     total += i
# print(total)

# N 찍기
# 문제
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# n = int(input())

# for i in range(1, n + 1):
#     print(i)

# 기찍 N
# 문제
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# n = int(input())

# for i in range(n, 0, -1):
#     print(i)

# 별 찍기 - 1
# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# n = int(input())

# for i in range(1, n+1):
#     print('*' * i)

# 구구단
# 문제
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# n = int(input())

# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')

# X보다 작은 수
# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 10 5
# 1 10 4 9 2 3 8 5 7 6

# 1 4 2 3

# n, x = map(int, input().split())
# a = list(map(int, input().split()))

# for i in a:
#     if x > i:
#         print(i, end=" ")

# 음계
# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

# num = list(map(int, input().split()))

# if num == sorted(num):
#     print('ascending')
# elif num == sorted(num, reverse=True):
#     print('descending')
# else:
#     print('mixed')
