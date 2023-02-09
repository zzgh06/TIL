# 10866 : 덱
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# from collections import deque
# import sys

# dq = deque()
# n = int(input())

# for _ in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == 'push_front':
#         dq.appendleft(int(command[1])) # 문자열로 입력되었기 때문에 정수로 변환하여 출력
#     elif command[0] == 'push_back':
#         dq.append(int(command[1]))
#     elif command[0] == 'pop_front':
#         if dq: # dq 리스트라면(비어있지 않다면)
#             print(dq.popleft())
#         else:
#             print("-1")
#     elif command[0] == 'pop_back':
#         if dq:
#             print(dq.pop())
#         else:
#             print("-1")
#     elif command[0] == 'size':
#         print(len(dq))
#     elif command[0] == 'empty':
#         if dq:
#             print('0')
#         else:
#             print('1')
#     elif command[0] == 'front':
#         if dq:
#             print(dq[0])
#         else:
#             print('-1')
#     elif command[0] == 'back':
#         if dq:
#             print(dq[-1])
#         else:
#             print('-1')


# 2605 : 줄세우기 # 그냥 원하는 곳에 삽입하면 되는문제 .insert() 활용
# n = int(input())
# students = list(map(int, input().split()))
# arr = []

# for i in range(n): # 0~4
#     arr.insert(students[i], i+1)

# print(*arr[::-1])


# 2644 : 촌수계산
# n = int(input()) # 전체 사람의 수
# a, b = map(int, input().split()) # 촌수를 계산해야하는 서로 다른 두 사람의 번호
# m = int(input()) # 부모 자식들 간의 관계의 개수
# graph = [[] for _ in range(n+1)] # 인접리스트를 만들기 위한 빈 리스트 생성
# visited = [False] * (n+1) # 방문 처리 리스트
# stack = [] # 결과를 담을 빈 리스트

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x) 

# def dfs(start, num): # 검사를 시작할 정점 7, 0
#     num += 1 # 0부터 순차대로 검사하기 위한 변수
#     visited[start] = True # 정점 방문처리 : 7
    
#     if start == b: # start 와 b의 값이 같을때
#         stack.append(num) # stack에 num 추가
    
#     for adj in graph[start]: # 인접한 모든 정점에 대해
#         if not visited[adj]: # 아직 방문하지 않았다면
#             dfs(adj, num) # def dfs(start, num) < (adj, num)로 교체

# dfs(a, 0) # 검사를 시작할 정점

# if len(stack) == 0:
#     print(-1)
# else:
#     print(stack[0]-1)