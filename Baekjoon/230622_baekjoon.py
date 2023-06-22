# 단어 공부
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 
# 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# a = input().upper() # Baaa => BAAA
# alpha = list(set(a)) # ['B', 'A']
# alpha_list = []

# for i in alpha:
#     cnt = a.count(i) # 1, 3 또는 3, 1 Set 때문에 중복제거하면서 랜덤으로 배열
#     alpha_list.append(cnt) # ['1', '3'] 또는 ['3', '1']

# if alpha_list.count(max(alpha_list)) > 1: # 최대 값이 1개 이상일 경우
#     print('?')
# else:
#     max_index = alpha_list.index(max(alpha_list)) # 최대 값의 위치를 max_index
#     print(alpha[max_index]) 


# 베스트셀러
# 문제
# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
# 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 
# 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 
# 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
# import sys
# input = sys.stdin.readline

# n = int(input())
# sell = {}

# for i in range(n):
#     book = input()
#     if book not in sell:
#         sell[book] = 1
#     else:
#         sell[book] += 1

# max_value = max(sell.values())

# best = []

# for key, value in sell.items():
#     if value == max_value:
#         best.append(key)
# best = sorted(best)
# print(best[0])