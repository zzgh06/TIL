# 2167 : 2차원 배열의 합
# 배열의 크기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr) [[1, 2, 4], [8, 16, 32]]

# 부분의 개수
k = int(input())
dp = [[0] * (m+1) for _ in range(n+1)]
# print(dp) [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] # 2차원 배열 누적합 공식 [[0, 0, 0, 0], [0, 1, 3, 7], [0, 9, 27, 63]]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]) # (i, j) (x,y) 범위 주위를 둘러싼 누적합을 빼주고 교집합을 더해준다
