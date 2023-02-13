# 6061
# a, b = map(int, input().split())
# print(a|b)

# 6062
# a, b = map(int, input().split())
# print(a^b)

# 6063
# n = list(map(int, input().split()))
# print(max(n))

# 6064
# n = list(map(int, input().split()))
# print(min(n))

# 6065
# n = list(map(int, input().split()))
# for i in n:
#     if i%2 == 0:
#         print(i)

# 6066
# n = list(map(int, input().split()))
# for i in n:
#     if i%2 == 0:
#         print('even')
#     else:
#         print('odd')

# 6067
# n = int(input())

# if n<0:
#     if n%2 == 0:
#         print('A')
#     else:
#         print('B')
# else:
#     if n%2 == 0:
#         print('C')
#     else:
#         print('D')

# 6068
# n = int(input())

# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D') 

# 6069
# s = input()

# if s == 'A':
#     print('best!!!')
# elif s == 'B':
#     print('good!!')
# elif s == 'C':
#     print('run!')
# elif s == 'D':
#     print('slowly~')
# else:
#     print('what?')

# 6070
# n = int(input())

# if n//3 == 1:
#     print("spring")
# elif n//3 == 2:
#     print("summer")
# elif n//3 == 3:
#     print("fall")
# else:
#     print("winter")

# 6071~2
# n = int(input())
# while True:
#     print(n)
#     n = n - 1
#     if n == 0:
#         break

# 6073
# n = int(input())
# while True:
#     n = n - 1
#     print(n)
#     if n == 0:
#         break

# 6074
# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1

# 6075~6
# n = int(input())

# for i in range(n+1):
#     print(i)

# 6077
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         s += i
# print(s)

# 6078
# while True:
#     s = input()
#     print(s)

#     if s == 'q':
#         break

# 6079
# n = int(input())
# num = 0
# for i in range(1, n+1):
#     num += i
#     if num >= n:
#         print(i)
#         break

# 6080
# n, m = map(int, input().split())

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# 6081
# n = int(input(), 16)

# for i in range(1, 16) :
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082
# n = int(input())
# for i in range(1, n+1) :
#     if i%10 == 3 or i%10 == 6 or i%10 == 9:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')

# 6083
# a, b, c = list(map(int, input().split()))
# cnt = 0

# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             print('%d %d %d' %(i,j,k))
#             cnt += 1
# print(cnt)

# 6084
# h, b, c, s = map(int, input().split())
# print(round(h*b*c*s/8/1024/1024, 1), "MB")

# 6085
# w, h, b = input().split()
# res = int(w)*int(h)*int(b)/1024/1024/8
# print('%.2f'%res,"MB")

# 6086
