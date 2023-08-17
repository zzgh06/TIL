# 1926 : 그림

# 문제
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

# 입력
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

# 출력
# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 
# 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다

# 아이디어
# 1. 이중 for문을 통해 순회하면서 1 이면서, 아직 방문하지 않은 노드
# 2. bfs을 돌면서 그림 갯수, 가장 넓은 값
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    rs += 1
                    q.append((ny, nx))
    return rs



cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)


# 2667 : 단지번호 붙이기
# 아이디어
# 2중 for, 값 1 && 방문x => dfs
# dfs를 통해 찾은 값을 저장 후 정렬해서 출력

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
res = []
each = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            res.append(each)

res.sort()
print(len(res))
for i in res:
    print(i)