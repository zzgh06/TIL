import sys
input = sys.stdin.readline
matrix = [list(map(int, input().split())) for _ in range(9)] # 2차원 리스트를 통해 행렬 생성

x = 0 # 인덱스 확인을 위한 변수 생성
y = 0
max_num = 0 # 최대값 확인을 위한 변수 생성

for i in range(9): # 행우선 순회
    for j in range(9):
        if matrix[i][j] >= max_num: # 순회하면서 max_num 변수 값보다 클 경우(최댓값이 두 개 이상인 경우도 있기 때문에 '>='를 사용한다 )
            max_num = matrix[i][j] # matrix[i][j] 값을 max_num 변수 값으로 변경한다 
            x = i + 1 # 시작기준이 1행 1열 이여서 i와 j 값에 1씩 더한다
            y = j + 1

print(max_num)
print(x, y)
