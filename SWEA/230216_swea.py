# 3431. 준환이의 운동관리
# T = int(input())

# for tc in range(1, T+1):
#     l, u, x = map(int, input().split())
#     if l <= x <= u:
#         print(f'#{tc}', 0)
#     elif x < l:
#         print(f'#{tc}', l-x)
#     else:
#         print(f'#{tc}', -1)

# 10505. 소득 불균형
# T = int(input())

# for tc in range(1, T+1):
#     n = int(input())
#     s = list(map(int, input().split()))
#     sum = 0
#     for i in s:
#         sum += int(i)
#     average = sum/n
#     cnt = 0
#     for j in s:
#         if int(j) <= average:
#             cnt += 1
#     print(f'#{tc}', cnt)

# 4406. 모음이 보이지 않는 사람
# T = int(input())

# for tc in range(1, T+1):
#     str = input()

#     gather = ['a', 'e', 'i', 'o', 'u']
#     for i in gather:
#         if i in str:
#             str = str.replace(i, '')
#     print(f'#{tc}', str)