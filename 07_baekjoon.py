# 개수 세기
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다

# cnt = 0
# num = int(input())
# numbers = map(int, input().split())
# v = int(input())
# for i in numbers:
#     if i == v:
#         cnt += 1
# print(cnt)

# 과제 안 내신 분..?

# students = [i for i in range(1,31)] 
# # i for i in range() 이렇게 쓰면 range 함수의 범위만큼 한줄에 출력할 수 있다

# for n in range(28):
#     num = int(input())
#     students.remove(num)

# print(min(students))
# print(max(students))

# 문제 1 : 홀수
# number = []
# for i in range(7):
#     n = int(input())
#     if n % 2 == 1: # 홀수를 구하기 위해 조건문을 통해 정수 n를 2로 나눴을 때 나머지가 1이 되는 정수를 선택하고 
#         number.append(n) # 이를 append()를 통해 number 리스트에 넣는다

# print(sum(number)) # 입력 값 n 중 홀수만 들어간 number 리스트를 sum 함수를 통해 더해주고
# print(min(number)) # 마찬가지로 min 함수를 통해 number 리스트 중 가장 작은 수를 출력한다

# 문제 2 : 더하기
# print(sum(map(int, input().split(',')))) 

# 한줄 입력가능, 공백 기준을 ','으로 하여 입력값을 나눠주고 이를 int 함수로 정수로 변경하여
# sum 함수를 통해 합쳐 출력한다 

# 문제 3 : 학점계산

# result = {
#     'A+' : 4.3, 'A0' : 4.0, 'A-' : 3.7,
#     'B+' : 3.3, 'B0' : 3.0, 'B-' : 2.7,
#     'C+' : 2.3, 'C0' : 2.0, 'C-' : 1.7,
#     'D+' : 1.3, 'D0' : 1.0, 'D-' : 0.7,
#     'F' : 0.0}

# grade = input()
# print(result[grade])

# 문제 4 : 다이얼

# numbers = {
#     2 : "ABC", 3 : "DEF",
#     4 : "GHI", 5 : "JKL", 6 : "MNO",
#     7 : "PQRS", 8 : "TUV", 9 : "WXYZ",
# }

# dial = input().upper() # upper() 메서드를 통해 입력된 문자열을 대문자로 변경
# time = 0

# for i in dial: # 반복문을 통해 입력된 문자열을 순회하고 
#     for key, value in numbers.items(): # .items() 메서드를 통해 numbers 딕셔너리의 key와 value 값을 순회하며 
#         if i in value: # 그 중 value 안의 순회하는 i 문자열이 들어가 있다면  
#             time += key + 1 # key 값에 + 1 하여 time 변수에 담는다, +1를 해준 이유는 2는 3초, 3는 4초 등 1씩 증가하기 때문   

# print(time)

# 문제 5 : 숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())

# total = str(a * b * c) # 입력 받은 a, b, c를 * 연산자로 곱하고 이를 str 함수를 통해 문자열로 변경(count 메서드 사용을 위해)하여 total 변수에 대입한다.

# for i in range(10): # 반복문을 통해 0 ~ 9 순회하면서
#     print(total.count(str(i))) 
    # 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력하는게 목표이기 때문에
    # .count() 메서드를 통해 i (0~9)가 total 변수에 몇 개씩 들어갔는지 개수를 측정한다. 
    # count() 메서드는 문자열 메서드이기 때문에 str 함수를 통해 i 값을 문자열로 변경한다 