# 10871 : X보다 작은 수
# n, x = map(int, input().split())
# numbers = list(map(int, input().split()))

# for i in numbers:
#     if x > i:
#         print(i, end=" ")

# 2789 : 유학금지
# str = input()
# alpha = 'CAMBRIDGE'

# for i in alpha:
#     if i in str:
#         str = str.replace(i, '')
# print(str)

# 1357 : 뒤집힌 덧셈
# x, y = input().split()
# x = int(x[::-1])
# y = int(y[::-1])
# print(int(str(x+y)[::-1]))

# 2908 : 상수
# a, b = input().split()
# a = a[::-1]
# b = b[::-1]
# if int(a) > int(b):
#     print(a)
# else:
#     print(b)

# 11720 : 숫자의 합
# n = input()
# s = input()
# total = 0

# for i in s:
#     total += int(i)
# print(total)

# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
# T = int(input())

# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     print(f'#{tc}', n**m)