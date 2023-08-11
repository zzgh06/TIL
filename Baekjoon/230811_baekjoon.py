# 10026 : 적록색약
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == False:
            if graph[nx][ny] == color:
                dfs(nx, ny)

cnt1, cnt2 = 0, 0

for j in range(n):
    for k in range(n):
        if visited[j][k] == False:
            dfs(j, k)
            cnt1 += 1

for j in range(n):
    for k in range(n):
        if graph[j][k] == 'R':
            graph[j][k] = 'G'

visited = [[False] * n for _ in range(n)]

for j in range(n):
    for k in range(n):
        if visited[j][k] == False:
            dfs(j, k)
            cnt2 += 1

print(cnt1, cnt2)