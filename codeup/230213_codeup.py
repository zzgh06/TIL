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
# n = int(input())
# s = 0
# c = 0
# while True:
#     s += c
#     c += 1
#     if s >= n:
#         break
# print(s)

# 6087
# n = int(input())

# for i in range(1, n+1):
#     if i%3 != 0:
#         print(i, end=' ')

# 6088
# a, d, n = map(int, input().split())
# print(a+d*(n-1))

# 6089
# a, r, n = map(int, input().split())
# print(a*r**(n-1))

# 6090
# a, m, d, n = map(int,input().split())
# num=0
# for i in range(1,n):
#     a = (m*a)+d
# print(a)

# 6091
# a, b, c = map(int, input().split())
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)

# 6092
# n = int(input())      
# a = input().split() 

# for i in range(n) :  
#     a[i] = int(a[i])      

# d = []                     
# for i in range(24) :  
#     d.append(0)        

# for i in range(n) :    
#     d[a[i]] += 1

# for i in range(1, 24) : 
#     print(d[i], end=' ')

# 6093
# n = int(input())
# a = list(map(int, input().split()))
# for i in range(n-1, -1, -1) :
#     print(a[i], end=' ')

# 6094
# n = int(input())
# a = list(map(int, input().split()))

# a_l = sorted(a)
# print(a_l[0])

# 6095
# d=[]                        
# for i in range(20) :
#   d.append([])        
#   for j in range(20) : 
#     d[i].append(0)    

# n = int(input())
# for i in range(n) :
#   x, y = map(int, input().split())
#   d[x][y] = 1

# for i in range(1, 20) :
#   for j in range(1, 20) : 
#     print(d[i][j], end=' ')    
#   print()  

# 6096
# d=[]
# for i in range(20) :
#   d.append([])
#   for j in range(20) : 
#     d[i].append(0)

# for i in range(19) :
#   a = input().split()
#   for j in range(19) :
#     d[i+1][j+1] = int(a[j])

# n = int(input())
# for i in range(n) :
#   x,y=input().split()
#   x=int(x)
#   y=int(y)
#   for j in range(1, 20) :
#     if d[j][y]==0 :
#       d[j][y]=1
#     else :
#       d[j][y]=0

#     if d[x][j]==0 :
#       d[x][j]=1
#     else :
#       d[x][j]=0

# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(d[i][j], end=' ')
#   print()

# 6097
# h, w = map(int, input().split())
# n = int(input())

# zeros = [[0] * w for _ in range(h)]

# for i in range(n):
#     l, d, x, y = map(int, input().split())

#     for j in range(l):
#         if d == 0:
#             zeros[x-1][y-1+j] = 1
#         else:
#             zeros[x-1+j][y-1] = 1

# for i in range(h):
#     for j in range(w):
#         print(zeros[i][j], end=' ')
#     print(end='\n')

# 6098
# array = []

# for i in range(10):
#     array.append(list(map(int, input().split())))

# x, y = 1, 1

# while True:
#     if (array[x][y] == 0):
#         array[x][y] = 9
#     elif (array[x][y] == 2):
#         array[x][y] = 9
#         break

#     if ((array[x][y+1] == 1 and array[x+1][y] == 1)):
#         break

#     if (array[x][y+1] != 1):
#         y = y + 1
#     elif (array[x+1][y] != 1):
#         x = x + 1

# for i in range(10):
#     for j in range(10):
#         print(array[i][j], end=' ')
#     print()
