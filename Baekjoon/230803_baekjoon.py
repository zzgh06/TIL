# 그림
# 문제
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 
# 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
# 그림의 넓이란 그림에 포함된 1의 개수이다.

# 1. 아이디어
# - 2중 for => 1 && 방문하지 않은 노드
# - BFS 돌면서 그림 개수 +1, 최대값을 갱신

# 2. 시간 복잡도
# - bfs : O(V+E)
# - V : 500 * 500
# - E : 4 * 500 * 500
# - V+E : 5 * 250000 = 100만 < 2억 >> 가능 

# 3. 자료구조
# - 그래프 전체 지도 : int[][]
# - 방문 : bool[][]
# - Queue(BFS)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # bfs > 그림 크기를 구해주고
            # 최대값 갱신
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
