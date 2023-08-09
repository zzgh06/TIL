# 1260 : DFS와BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다.

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

def dfs(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited2[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)