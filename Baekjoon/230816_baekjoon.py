# 2644 : 촌수계산

n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = []
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, cnt):
    cnt += 1
    visited[v] = True
    
    if v == e:
        res.append(cnt)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)

dfs(s, cnt)

if len(res) > 0:
    print(res[0] - 1)
else:
    print(-1)