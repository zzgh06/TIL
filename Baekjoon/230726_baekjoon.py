# 2차원 배열의 합
# 문제
# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 
# 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
# 배열의 (i, j) 위치는 i행 j열을 나타낸다.

# 누적합과 부분합 알고리즘 활용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n) ]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n +1):
    for j in range(1, m +1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
