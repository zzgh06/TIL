# 1157 : 단어 공부
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# word = input().upper() # 대소문자로 된 단어가 주어지지만 대문자와 소문자를 구분하지 않기 때문에 upper 혹은 lower 를 통해 입력 값을 대문자 혹은 소문자로 변경한다
# word_list = list(set(word)) # 그리고 반복문에서 중복된 단어를 제외하여 순회하기 위해 set 함수를 통해 중복된 요소를 제거한다.
# cnt = []

# for i in word_list: # 입력값 중 중복된 단어는 제외하여 순회
#     cnt.append(word.count(i))

# if cnt.count(max(cnt)) > 1: # cnt 리스트 중 가장 큰 값이 1개보다 많을 경우 
#     print('?') # '?'를 출력
# else:
#     print(word_list[(cnt.index(max(cnt)))]) # 아닐 경우 word_list 리스트에 cnt 리스트 중 가장 큰 값에 해당하는 인덱스 값( : 숫자 최대 값) 위치 출력

# 2439 : 별 찍기 -2

# n = int(input())

# for i in range(1, n + 1):
#     result = ""
#     result += " " * (n - i)
#     result += "*" * i
#     print(result)

# 1181 : 단어정렬
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 조건 1) 길이가 짧은 것부터
# 조건 2) 길이가 같으면 사전 순으로
# 조건 3) 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# n = int(input())
# word = []
# for i in range(n):
#     word.append(input()) # n번 만큼 순회하면서 입력 값을 .append() 리스트 메서드를 통해 word 리스트에 추가
# word_list = list(set(word)) # 조건 3)를 충족하기 위해 중복되는 단어를 제외하기 위한 set 함수 사용, set은 딕셔너리로 묶이기 때문에 앞에 list 함수 사용하여 리스트로 변경

# sort_word = [] # set 함수 사용 시 순서가 없기 때문에 이를 새롭게 저장할 리스트 변수 생성
# for i in word_list: # word_list에 저장된 단어를 반복문을 통해 순회하여
#     sort_word.append((len(i), i)) # 조건 1)과 2)를 충족하기 위해  해당 단어의 (길이, 단어)를 2개의 인수 형태로 sort_word 리스트에 추가
# result = sorted(sort_word) # sorted 함수를 통해 이를 단어의 길이와 사전 순으로 정렬하여 result 변수에 리턴

# for len_word, word in result: # result 변수 리스트에 길이와 문자 2개의 인수로 저장되어 있기 때문에 단어만 출력하기 위해서
#     print(word)               # 반복문의 매개변수를 'len_word, word' 2개로 사용하여 그 중 word 만 출력

# 2751 : 수 정렬하기 2 
# import sys # n의 범위가 n(1 <= n <= 1,000,000)임으로 그냥 input를 받으면 시간초과 됨으로 import sys / sys.stdin.readline() 활용

# n = int(input())
# numbers = []

# for i in range(n): 
#     numbers.append(int(sys.stdin.readline())) # 입력되는 정수를 numbers 리스트에 추가 

# for i in sorted(numbers): # 이를 sorted 함수를 통해 오름차순으로 정렬
#     print(i)