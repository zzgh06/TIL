# 2047. 신문 헤드라인
# 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.
# [예제 풀이]
# The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
# 위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.
# THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.

# [풀이]
string = input()
print(string.upper()) 
# # .upper 문자열 변경함수를 사용하여 대문자로 변경해준다
# .upper() : 모두 대문자 / .lower() : 모두 소문자 / .swapcase() : 대소문자 서로 변경

# 2025. N줄덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# [예제]
# 주어진 숫자가 10 일 경우 출력해야 할 정답은,
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

# [풀이]
num = int(input())
sum = 0
for n in range(1, num + 1):
    print(n) # for문과 range를 사용하여 input 값을 1부터 10까지 나열
    sum += n + 0 # 나열된 1부터 10까지 하나씩 변수 sum에 더해짐
print(sum) # 따라서 프린트하면 55가 출력됨

# 2027. 대각선 출력하기
# 주어진 텍스트를 그대로 출력하세요.
# #++++
# +#+++
# ++#++
# +++#+
# ++++#

# [풀이]
for a in range(5): # 0 1 2 3 4
    for b in range(5): # 0(01234)1(01234)2(01234)3(01234)4(01234) for 문 안의 for 문이 순회하여 이러한 형태로 순회된다 
        if a == b: # 이때 변수 a와 b가 같을 경우 
            print('#', end="") # '#'를 출력하고
        else: # 그렇지 않을 경우
            print('+', end="") # '+'가 출력되도록 if, else 를 사용
    print() #  print()함수만 실행해도 줄바꿈이 실행됨.

# 2058. 자릿수 더하기
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# 입력 : 6789

# [풀이]
num = input() 
total = 0
for n in num:
    print(n) # 6 7 8 9
    total += int(n) # input 값(문자열)을 int()함수로 이용하여 정수로 형변환하여 for문과 total 변수를 이용하여 각 수를 합친다 
print(total) # 30

# 2019. 더블더블
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 입력 : 8

# [풀이]
num = int(input())
for n in range(num+1): # for문과 range 를 사용하여 0 ~ 8을 순회하도록하며
    print(2**n, end=" ") # 1 2 4 8 16 32 64 128 256
# 이를 산술연산자 **(거듭제곱)를 이용하여 2의 0승부터 8승 까지 나열되도록 설정(2를 곱한 값을 구하기 위해)


