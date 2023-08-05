# 단지번호붙이기

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
num = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

print(result)
num.sort()
for i in range(len(num)):
    print(num[i])