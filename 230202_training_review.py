# 1547 : 공
# 조건
# 1) 컵의 위치를 바꾼 방법 x 와 y (둘의 위치를 교환)
# 2) x 와 y의 값은 3보다 작거나 같다(x 와 y 값이 같을 수도 있다)

# m = int(input())
# cups = [0, 1, 0, 0]  # 인덱스는 0부터 시작되기 때문에 범위 내에서 진행하기 위해 리스트의 요소로 4개를 넣어준다.

# for _ in range(m):
#     x, y = map(int, input().split())
#     cups[x], cups[y] = cups[y], cups[x]  # 변수 x 와 y 값을 스왑

# print(cups.index(1))  # cups 리스트 내 공(1)이 들어간 인덱스 위치 값을 출력


# 5576 : 콘테스트
# 조건
# 10명 중 득점이 높은 사람에서 3명의 점수를 합산

# w = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
# k = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
# 입력 값을 10개씩 나눠 입력받고 이를 sorted를 통해 오름차순 정렬, reverse = True을 통해 뒤집고 상위 3명 점수를 출력한다

# w = sorted([int(input()) for _ in range(10)])[7:]
# k = sorted([int(input()) for _ in range(10)])[7:]
# 다른 방법으로 뒤집지 않고 [7:] 를 통해 뒤에 정렬된 상위 점수 3개를 통해 값을 구할 수 있다

# print(sum(w), sum(k))


# 2846 : 오르막길
# 조건
# 숫자가 커질 때 더하고 작아질 때, 0으로 초기화 한다.

# n = int(input())
# height = list(map(int, input().split()))
# temp = 0 # 임시로 저장할 변수(오르막 높이 간 차이를 임시로 저장)
# ans = [] # 오르막이 끝날때 그 값을 저장할 리스트

# for i in range(1, n): # 1 ~ 4
#     if height[i-1] < height[i]: # 이전 인덱스보다 다음 인덱스 값이 클 경우
#         temp += height[i] - height[i-1] # 현재 값에서 이전 값의 차이를 temp 임시 변수에 더하여 대입
#         if i == n-1: # 이전보다 값이 크면서 마지막 인덱스 값도 높을 경우(오르막길)
#             ans.append(temp) # ans 리스트에 대입, 위의 조건문이 없을 경우 temp 에 저장된 값이 리스트에 추가되지 못하고 종료된다.
#     else:
#         ans.append(temp) # 이전 값보다 현재 인덱스 값이 크지 않을 경우 리스트에 그 값을 추가하고
#         temp = 0 # temp 변수를 초기화

# print(max(ans)) # 리스트에 저장된 값 중 가장 큰 값을 출력한다


# 1251 : 단어 나누기
# 조건
# 1) 세 단어로 쪼갤 수 있는 경우의 수를 모두 실행
# 2) 모든 경우의 수를 뒤집은 후 다시 원래 순서로 합친 후에 리스트에 추가
# 3) 사전 순으로 출력

# word = list(input())
# result = []

# for i in range(1, len(word)-1): # 이중 반복문으로 세 단어로 쪼갤 수 있는 경우의 수를 모두 실행
#     for j in range(i+1, len(word)):
#         first = word[:i] # ['m', 'o', 'b', 'i', 't']
#         second = word[i:j] # ['o', 'b', 'i', 't', 'e']
#         third = word[j:] # ['l']
#     print(first, second, third)
#         first.reverse()  # .reverse는 리스트 함수로 각 단어를 뒤집는다
#         second.reverse()
#         third.reverse()

#         result.append(''.join(first + second + third)) # ''.join(리스트) 매개변수로 들어온 값을 합쳐서 반환해준다
#         result.sort() # 사전 순으로 출력하기 위해 .sort 함수로 사전 순으로 정렬

# print(result[0])


# word = input()
# result = []

# for i in range(len(word) - 2): # 길이가 1 이상인 3개의 단어로 구분해야함
#     for j in range(i + 1, len(word) - 1):
#         for k in range(j + 1, len(word)):
#             new_word = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1] # 모든 경우의 수를 뒤집은 후(역슬라이싱) 합친다
#             result.append(new_word) # 합친 new_word 변수를 result 리스트에 추가

# res_word = sorted(result) # sorted 함수를 통해 사전 순으로 정렬시킨 후에

# print(res_word[0]) # 0번째 단어를 출력한다
