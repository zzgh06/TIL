# 1. 신용카드 만들기 1
# 신용카드 번호는 룬 공식(LUHN Formula)을 만족해야합니다.
# 룬 공식이란 카드 번호에서 마지막 자리(열여섯번째) 숫자N을 구하는 공식입니다.

# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다.

# T = int(input())

# for t in range(1, T+1):
#     numbers = list(map(int, input().split()))
#     total = 0
#     # 홀수, 짝수 구분하여 total 변수에 더함
#     for n in range(0, len(numbers)):
#         if (n + 1) % 2 == 1:
#             total += numbers[n] * 2
#         else:
#             total += numbers[n]
#     # 나열된 정수 중 홀수 번째에 2를 곱하여 더한 값과, 짝수 번째를 더한 값을
#     # 10으로 나눴을 때 나머지가 0일 경우 0을 출력하고
#     # 아닐 경우 10에서 나머지 값을 빼준 값을 출력한다 
#     if total % 10 == 0:
#         print(f'#{t} 0')
#     else:
#         print(f'#{t} {10 - total % 10}')

# 2. 신용카드 만들기 2
# 신용 카드를 만들려면 아래 두 가지의 조건을 모두 만족해야 한다.

# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.

# T = int(input())

# for t in range(1, T+1):
#     card = input()
#     start_number = ['3', '4', '5', '6', '9']
#     # 입력된 카드번호 문자열의 인덱스 0번째 위치한 숫자가 start_number 리스트에 담긴 문자열
#     # 그리고 '-'를 제외한 문자열의 길이가 16인 경우 '1'를 출력하고, 아닐 경우 '0'을 출력
#     if card[0] in start_number and len(card.replace('-', '')) == 16:
#         print(f'#{t} 1')
#     else:
#         print(f'#{t} 0')

# 3. 문자열의 거울상 
# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

# T = int(input())

# for t in range(1, T+1):
#     s = input()
#     mirror = ''
#     # 문자열을 역슬라이싱하고 뒤집어 반복문을 통해 순회
#     for m in s[::-1]:
#         # 조건문을 통해 문자열 'b'일 경우 'd'을 mirror 변수에 더해준다, 다른 문자열도 마찬가지의 형태로 진행한다
#         if m == 'b':
#             mirror += 'd'
#         elif m == 'd':
#             mirror += 'b'
#         elif m == 'p':
#             mirror += 'q'
#         else:
#             mirror += 'p'
#     print(f'#{t} {mirror}')

# 2번째 방법, 딕셔너리 사용하여 각 입력할 문자열을 key, 해당 문자열의 반대 형태를 value로 형성한다. 
# dict_alpah = {
#     'b' : 'd',
#     'd' : 'b',
#     'p' : 'q',
#     'q' : 'p'
# }

# T = int(input())

# for t in range(1, T+1):
#     s = input()
#     # mirror 변수에 입력된 문자열을 역슬라싱한 것을 대입하고
#     mirror = s[::-1]
#     # 딕셔너리 value 값을 저장할 문자열 변수 text를 생성해준다
#     text = ''
#     for i in range(len(mirror)):
#         # 딕셔너리의 각 value 값을 차례대로 text 변수에 더하여 저장한다.
#         text += dict_alpah[mirror[i]]

#     print(f'#{t} {text}')

# 4. 소득불균형
# 통계 자료를 처리할 때, 평균이 전체 집단의 특징을 꼭 잘 표현하는 것은 아니다.
# 예를 들어, 대다수의 국가에서는 적은 수의 사람이 국가 전체 소득의 꽤 많은 부분을 차지하기 때문에,
# 해당 국가의 평균 소득은 보통 사람들의 소득보다 높은 경우가 많다.
# 당신은, n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

# T = int(input())

# for t in range(1, T+1):
#     n = int(input())
#     cnt = 0
#     income = list(map(int, input().split()))
#     average = sum(income)//n
    
#     for num in income:
#         if num <= average:
#             cnt += 1
#     print(f'#{t} {cnt}')

# 4. 직사각형 길이 찾기
# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.
# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.
# 세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.
# 입력으로 직사각형이 불가능한 경우는 주어지지 않는다.

# T = int(input())

# for t in range(1, T+1):
#     a, b, c = list(map(int, input().split()))
#     if a == b:
#         d = c
#     elif a == c:
#         d = b
#     else:
#         d = a
#     print(f'#{t} {d}')

# 5. 최빈수 구하기


        