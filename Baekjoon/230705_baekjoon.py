# 피시방 알바
# 문제
# 세준이는 피시방에서 아르바이트를 한다. 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.

# 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다. 따라서 들어오면서 번호를 말한다. 
# 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.

# 거절당하는 사람의 수를 출력하는 프로그램을 작성하시오. 
# 자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.

# n = int(input()) # 손님의 수 N # 3
# customer = list(map(int, input().split())) # 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리 # 1 2 3
# pc = [0] * 101 # N은 100보다 작거나 같다
# cnt = 0 # 거절당하는 사람의 수

# for i in customer: # 1 2 3
#     if pc[i] != 0:
#         cnt += 1
#     else:
#         pc[i] += 1
# print(cnt)


# OX퀴즈
# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

tc = int(input())

for i in range(tc):
    ox = input()
    res = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == "O":
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)

