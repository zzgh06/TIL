# 예제 3-1 : 거스름돈
# n = int(input())
# cnt = 0
# coin = [500, 100, 50, 10]

# for i in coin:
#     cnt += n // i
#     n %= i

# print(cnt)

# 문제 1 : 큰 수의 법칙
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort() # 오름차순으로 정렬
# first = data[n-1] # 가장 큰수
# second = data[n-2] # 두번째로 큰수

# result = 0

# while True:
#     for i in range(k): # 가장 큰 수를 k번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1 # 더 할때 마다 1씩 빼기
#     if m == 0:
#         break
#     result += second # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더 할때마다 1씩 빼기 

# print(result)
