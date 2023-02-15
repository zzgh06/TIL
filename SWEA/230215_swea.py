# 1926. 간단한 369게임
# n = int(input())

# for i in range(1, n+1):
#     i = str(i)
#     cnt = 0
#     for j in range(len(i)):
#         if i[j] == '3' or i[j] == '6' or i[j] == '9':
#             cnt += 1
#     if cnt == 0:
#         print(i, end=' ')
#     elif cnt != 0:
#         print('-'*cnt, end=' ')

# 1986. 지그재그 숫자
# T = int(input())

# for tc in range(1, T+1):
#     n = int(input())
#     total = 0
#     for i in range(1, n+1):
#         if i%2 == 0:
#             total -= i
#         else:
#             total += i

#     print(f'#{tc}', total)

# 1284. 수도 요금 경쟁
# T = int(input())

# for tc in range(1, T+1):
#     p, q, r, s, w = map(int, input().split())
#     if w > r:
#         A = w*p
#         B = q + (w-r)*s
#     else:
#         A = w*p
#         B = q

#     if A > B:
#         print(f'#{tc}', B)
#     else:
#         print(f'#{tc}', A)

# 12368. 24시간
# T = int(input())

# for tc in range(1, T+1):
#     a, b = map(int, input().split())
#     if a+b >= 24:
#         print(f'#{tc}', (a+b)-24)
#     else:
#         print(f'#{tc}', a+b)

# 13218. 조별과제
# T = int(input())

# for tc in range(1, T+1):
#     n = int(input())
#     print(f'#{tc}', n//3)