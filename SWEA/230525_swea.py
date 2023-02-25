T = int(input())

for tc in range(1, T+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    # 델타(우하좌상 : 달팽이 방향으로)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0  # 시작점
    num = 1
    direction = 0  # 방향

    for i in range(n*n):
        snail[x][y] = num  # 순회하면서 각 현재 위치에 num를 대입
        num += 1  # 변수 값을 1씩 증가
        nx, ny = x + dx[direction], y + dy[direction]  # 다음 이동할 위치를 계산
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:  # 해당 위치가 유효하면
            x, y = nx, ny  # 해당위치로 이동
        else:
            # 이동 방향을 바꾸고(direction 값이 3일 때, 1 증가시키면 4가 되어버리므로, 이를 위해 % 연산자를 사용하여 4로 나눈 나머지 값을 다시 direction 변수에 저장)
            direction = (direction + 1) % 4
            x, y = x + dx[direction], y + dy[direction]  # 다시 다음 이동할 위치를 계산하여 이동

    # 달팽이 출력
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()
