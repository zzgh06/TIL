# 10769 : 행복한지 슬픈지
# 어떤 이모티콘도 포함되어 있지 않으면, none 을 출력한다.
# 행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, unsure 를 출력한다.
# 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, happy 를 출력한다.
# 슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, sad 를 출력한다.

# s = input()
# happy = s.count(':-)')
# sad = s.count(':-(') 
# # 이모티콘 개수를 비교하기 위해 입력받은 문자열을 count() 문자열 메소드를 사용하여 개수를 비교한다

# if happy == 0 and sad == 0:
#     print('none')
# elif happy == sad:
#     print('unsure')
# elif happy > sad:
#     print('happy')
# else:
#     print('sad')


# 2455 : 지능형 기차
# 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을때(max)

# train = [] # 각 역마다 인원수를 저장할 리스트
# cnt = 0 # 인원수를 저장할 변수

# for _ in range(4): # 4개역
#     a, b = map(int, input().split())
#     cnt += b - a # 탄사람수 - 내린사람수
#     train.append(cnt)

# print(max(train))

# 2606 : 바이러스
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
# n = int(input()) # 정점 개수
# m = int(input()) # 간선 개수
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1) # 양방향

# visited = [False] * (n+1)

# def dfs(start):
#     stack = [start]
#     visited[start] = True # 1번 방문처리

#     while stack: # 스택이 빌때까지
#         cur = stack.pop()

#         for adj in range(cur): # 첫 노드와 인접한 노드 
#             if not visited[adj]: # 방문하지 않았다면
#                 visited[adj] = True # 방문처리
#                 stack.append(adj) # 인접노드를 스택에 추가하여 기록, 처음으로 돌아가 스택의 마지막 요소를 삭제

# dfs(1)
# print(sum(visited)-1) # [False, True, True, True, False, True, True, False] # 1번 컴퓨터를 통해 감연된 컴퓨터 수를 구하는 것이기 때문에 -1를 해준다

