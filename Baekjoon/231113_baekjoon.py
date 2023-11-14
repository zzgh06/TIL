# 최솟값 찾기

# 문제
# N개의 수 A1, A2, ..., AN과 L이 주어진다.

# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

# 입력
# 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)

# 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

# 예제 입력
# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6

from collections import deque
n, l = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(n):
    while mydeque and mydeque[-1][0] > now[i]: # mydeque에 원소가 존재하면서, mydeque에 마지막 위치의 값이 현재 들어오는 값보다 클 경우 제거
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - l:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')