# 1302 : 베스트셀러 # 해시를 사용한 집합과 맵
# books = {} # 빈 딕셔너리 생성
# for _ in range(int(input())): 
#     book = input() # 책 제목 입력
#     if book not in books: # 딕셔너리에 입력 값이 없을 경우
#         books[book] = 1 # 빈 딕셔너리에 키와 밸류 값을 저장
#     else:
#         books[book] += 1 # 입력 값이 존재할 경우, 밸류 값에 1씩 더함

# max_book = max(books.values()) # 딕셔너리에 저장된 값 중, 판매량을 나타내는 value 값 중 가장 큰 값을 변수에 저장
# best = [] # 가장 많이 판매된 책을 저장할 리스트 생성

# for book, number in books.items(): # items를 사용하여 튜플의 형태로 비교
#     if number == max_book: # 딕셔너리에 저장된 value 값이 max_book 변수에 저장된 가장 큰 값이 일치할 경우
#         best.append(book) # 빈리스트에 그 제목(key)을 추가
# print(sorted(best)[0]) # 이를 정렬하여(사전순), 가장 첫번째 값을 출력(판매량이 동일할 경우 사전순이 빠른 값을 출력) 


# 20291 : 파일 정리
# import sys
# input = sys.stdin.readline

# f_list = {}
# for _ in range(int(input())):
#     f = (input().split('.'))[1] # 입력값을 '.'을 기준으로 분리하면 리스트 형태로 저장되어([sbrus, txt]) 그 중 확장자를 의미하는 1번째 인덱스 값을 변수 f에 저장
#     if f not in f_list: # 변수 f 값이 빈 딕셔너리 안에 없다면
#         f_list[f] = 1 # 딕셔너리에 저장
#     else:
#         f_list[f] += 1 # 존재할 경우, value 값에 1씩 더함.

# sort_file = sorted(f_list.items()) # 딕셔너리 정렬할 때, items 메서드를 사용해야됨

# for key, value in sort_file:
#     print(key.rstrip(), value) # rstrip를 사용하여 오른쪽 공백을 제거해야 키와 밸류 값이 나란히 출력됨

