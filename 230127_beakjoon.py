# 20001 : 고무오리 디버깅 # stack 문제
# stack = []

# while True:
#     s = input()
#     if s == '문제':
#         stack.append(s)
#     elif s == '고무오리':
#         if len(stack) == 0: # 고무오리가 입력되었을 때, stack 리스트가 비어있다면, 문제를 2번 추가
#             stack.append(s)
#             stack.append(s)
#         else:
#             stack.pop()
#     else:
#         if s == '고무오리 디버깅 끝':
#             break

# if len(stack) == 0:
#     print('고무오리야 사랑해')
# else:
#     print('힝구')


# 1269 : 대칭 차집합 # set 활용문제
# a, b = map(int, input().split())

# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# print(len(A - B) + len(B - A))


# 3025 : 나머지 # set 활용문제
# mod = []

# for i in range(10):
#     n = int(input())
#     mod.append(n % 42)
    
# print(len(set(mod)))


# 1181 : 단어 정렬 # set, sorted, 튜플활용
# 조건 1) 길이가 짧은 것부터
# 조건 2) 길이가 같으면 사전 순으로
# 조건 3) 중복된 단어는 한 번씩만 출력
# n = int(input())
# words = []

# for i in range(n):
#     s = input()
#     words.append(s)
# word = set(words)

# word_sort = []
# for i in word:
#     word_sort.append((len(i), i))
# word_li = sorted(word_sort)

# for key, value in word_li:
#     print(value)


# 11286 : 절대값 힙 # import heapq, abs(), 튜플 활용

# 조건 1) 배열에 정수 x (x != 0)를 넣는다
# 조건 2) 배열에서 절대 값이 가장 작은 값을 출력, 그 값을 배열에서 제거
# 조건 3) 만약 배열이 비어있는 경우 0를 출력
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# heap = []

# for i in range(n):
#     x = int(input())
#     if x != 0:
#         heapq.heappush(heap, (abs(x), x)) 
#         # 절대 값을 기준으로 정렬되어야 하기 때문에, 튜플의 형태로 리스트에 추가하며, 
#         # 튜플은 비교할 때 첫번째 원소를 기준으로 정렬하기 때문에 (절댓값, 실제 값) 튜플 형식으로 heap에 넣는다
#         # print(heap) # [(1, -1), (1, -1), (1, -1), (1, 1), (1, 1), (1, 1), (2, 2), (2, -2)]
#     else: # x 입력 값이 0 이면서
#         if len(heap) != 0: # heap 리스트가 비어있지 않다면
#             print(heapq.heappop(heap)[1]) 
#             # 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거 
#             # 이때 출력은 실제 값으로 해야하기 때문에 인덱스 [1]를 출력
#         else:
#             print(0) # heap 리스트가 비어있다면 0를 출력함
