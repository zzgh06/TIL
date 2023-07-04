# 나머지
# 문제
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

# 1
# res = []

# for _ in range(10):
#     n = int(input())
#     if n % 42 not in res:
#         res.append(n % 42)
# print(len(res))

# 2
# arr = []

# for _ in range(10):
#     n = int(input())
#     arr.append(n % 42)

# res = set(arr)
# print(len(res))


# 듣보잡
# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, 
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.
n, m = map(int, input().split())
a = set()
b = set()

for i in range(n):
    a.add(input())

for i in range(m):
    b.add(input())

res = sorted(list(a & b))
print(len(res))

for i in res:
    print(i)