# 6007
# print('"C:\\Download\\\'hello\'.py"')

# 6008
# print("print(\"Hello\\nWorld\")")

# 6009
# a = input()
# print(a)

# 6010
# n = input()
# print(int(n))

# 6011
# f = float(input())
# print(f)

# 6012
# a = int(input())
# b = int(input())
# print(a, b, sep='\n')

# 6013
# a = input()
# b = input()
# print(b, a, sep='\n')

# 6014
# f = float(input())
# for _ in range(3):
#     print(f)

# 6015
# a, b = map(int, input().split())
# print(a, b, sep='\n')

# 6016
# a, b = input().split()
# print(b, a)

# 6017
# s = input().split()
# print(*s*3)

# 6018
# a, b = input().split(':')
# print(a, b, sep=':')

# 6019
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

# 6020
# a, b = input().split('-')
# print(a+b)

# 6021
# s = input()
# for i in s:
#     print(i)

# [print(i) for i in input()]

# 6022
# s = input()
# print(s[0:2], s[2:4], s[4:])

# 6023
# s = input().split(':')
# print(s[1])

# 6024
# a, b = input().split()
# print(a+b)

# 6025
# a, b = map(int, input().split())
# print(a+b)

# 6026
# a = float(input())
# b = float(input())
# print(a + b)

# 6027
# n = int(input())
# print('%x'% n)
# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)

# 6028
# n = int(input())
# print('%X'% n)

# 6029
# a = input()
# n = int(a, 16) # 입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o' % n) # n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

# 6030
# n = ord(input()) # 입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# print(n)

# 6031
# c = int(input()) # c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.
# print(chr(c))
# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.

# 6032
# n = int(input())
# print(-n)

# 6033
# n = input()
# c = ord(n)
# print(chr(c+1))

# 6034
# a, b = map(int, input().split())
# print(a + (-b))

# 6035
# a, b = map(float, input().split())
# print(a*b)

# 6036
# a, b = input().split()
# print(a * int(b))

# 6037
# n = input()
# s = input()
# print(int(n)*s)

# 6038
# a, b = map(int, input().split())
# print(a**b)

# 6039
# a, b = map(float, input().split())
# print(a**b)

# 6040
# a, b = map(int, input().split())
# print(a//b)

# 6041
# a, b = map(int, input().split())
# print(a%b)

# 6042
# n = float(input())
# print(round(n, 2))

# 6043
# a, b = map(float, input().split())
# print("%0.3f" % (a/b))

# 6044
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b) # 몫
# print(a%b) # 나머지
# print(round(a/b, 2))

# 6045
# a, b, c = map(int, input().split())
# add = a + b + c
# average = add / 3

# print(add, format(average, "0.2f"))

# 6046
# n = int(input())
# print(n<<1)
# n = 10
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 6047
# a, b = map(int, input().split())
# print(a<<b)

# 6048
# a, b = map(int, input().split())
# if a < b:
#     print('True')
# else:
#     print('False')

# 6049
# a, b = map(int, input().split())
# print('True' if a == b else 'False')

# 6050
a, b = map(int, input().split())
print('True' if b >= a else 'False')