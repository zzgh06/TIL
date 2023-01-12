# 2025. N줄덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.

# number = int(input())
# total = 0
# for num in range(1, number+1): # for문을 통해 1~10까지 순회되도록 하며
#     total += num # 이를 등차수열 처럼 차례대로 합치기 위해 total 변수안에 차례대로 쌓여가도록 함
# print(total)

# 2029. 몫과 나머지 출력하기
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

# T = int(input())
# for t in range(1, T+1):
#     a, b = list(map(int, input().split()))
#     print(f'#{t} {a//b} {a%b}')

# 1545. 거꾸로 출력해 보아요
# 주어진 숫자부터 0까지 순서대로 찍어보세요

# number = int(input())

# for num in range(number, -1, -1):
#     print(num, end=" ")

# 1859. 백만 장자 프로젝트
# 25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
# 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#     1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#     2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#     3. 판매는 얼마든지 할 수 있다.

# 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     n_list = list(map(int, input().split()))
#     sell_price = 0
#     maximum_profit = 0

#     for max_price in n_list[::-1]:
#         if max_price >= sell_price:
#             sell_price = max_price
#         else:
#             maximum_profit += sell_price - max_price
#     print(f'#{t} {maximum_profit}')