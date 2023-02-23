# 6057 : 설탕과자 뽑기
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
h, w = map(int, input().split())
n = int(input())

matrix = [[0] * w for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())

    for i in range(l):
        if d == 0: # 가로 일때(열만 이동)
            matrix[x-1][y-1+i] = 1
        else: # 세로 일때(행만 아동)
            matrix[x-1+i][y-1] = 1

for i in range(h): # 모든 막대를 놓은 격자판의 상태를 출력
    for j in range(w):
        print(matrix[i][j], end=' ')
    print()