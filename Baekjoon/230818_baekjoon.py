# 15649 : N과 M(알고리즘 : 백트래킹)

# 아이디어
# 백크래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
# 재귀함수에서 m개를 선택할 경우 print

# 시간복잡도
# n^n : 중복이 가능, n=8까지 가능
# n! : 중복이 불가, n=10까지 가능

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
chk = [False] * (n + 1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n + 1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num + 1)
            chk[i] = False
            rs.pop()

recur(0)