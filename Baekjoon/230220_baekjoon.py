# 10816 : 숫자 카드2 # 이분탐색 # 해시를 사용한 집합과 맵
# import sys
# input = sys.stdin.readline
# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# cnt_card = list(map(int, input().split()))

# card_list = {}
# for card in cards:
#     if card not in card_list:
#         card_list[card] = 1
#     else:
#         card_list[card] += 1
# # print(cnt_card) {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}
# for i in cnt_card:
#     result = card_list.get(i) # GET 함수 : 딕셔너리의 get(x) 함수는 x라는 key에 대응되는 value값을 돌려준다.
#     if result == None:
#         print(0, end=" ")
#     else:
#         print(result, end=" ")

# 1822 : 차집합
# a, b = map(int, input().split())

# a_set = set(list(map(int, input().split()))) # set 함수를 통해 집합형태로 저장
# b_set = set(list(map(int, input().split())))

# res = a_set - b_set # 두 집합을 빼서 차집합의 결과를 변수에 저장 

# sort_res = sorted(res) # 이를 정렬시킴(set 함수 사용하면 정렬이 되지 않고 뒤죽박죽)
# print(len(sort_res))

# if len(sort_res) != 0:
#     print(*sort_res)

# 1764 : 듣보잡
# n, m = map(int, input().split())
# a = set()
# b = set()

# for _ in range(n):
#     a.add(input()) # set에 요소를 추가할 때는 add 메서드 사용
# for _ in range(m):
#     b.add(input())

# result = sorted(list(a & b)) # 교집합을 통해 중복된 값을 변수 저장
# print(len(result))

# for i in result:
#     print(i)