# 민석이의 과제 체크하기
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성

# T = int(input())

# for tc in range(1, T+1):
#     n, k = map(int, input().split())  # 수강생 수, 과제 제출한 사람의 수
#     submit = list(map(int, input().split()))  # 과제를 제출한 사람의 번호
#     result = []  # 제출하지 않은 인원의 번호를 담을 리스트 생성

#     for i in range(1, n+1):  # 1번 ~ 5번까지 순차적으로 순회
#         if i not in submit:  # not in 연산자를 통해 1~5까지 들어가 있지 않은 번호를
#             result.append(i)  # result 리스트에 추가
#     print(f'#{tc}', *result)


# 파리퇴치
# N x N 배열, M x M 크기의 파리채, 최대한 많은 파리를 죽이고자 한다

# T = int(input())

# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     kill = [] # 파리채를 범위별로 차례대로 휘둘렀을 때, 죽인 파리의 수를 저장할 리스트

#     for i in range(n-m+1): # 파리채의 크기에 따라 범위가 넘어갈 수 있어 범위를 n-m+1로 지정
#         for j in range(n-m+1):
#             fly = 0 # 죽인 파리를 더할 변수를 생성

#             for k in range(m):
#                 for l in range(m):
#                     fly += matrix[i+k][j+l]
#                     kill.append(fly) # 죽인 파리를 더하여 대입한 변수 fly의 값을 kill 리스트에 추가

#     print(f'#{tc}', max(kill)) # 최대한 많은 파리를 죽이고자 했으니 리스트에 저장된 값 중 max를 통해 가장 큰 값을 출력


# 조교의 성적 매기기

# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     students_total = [] # 학생들의 점수를 저장할 리스트
#     grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 성적 등급

#     for i in range(N):
#         mid, final, ass = map(int, input().split())
#         total = (mid * 0.35) + (final * 0.45) + (ass * 0.20) # 중간, 기말, 과제별 반영되는 점수를 통해 총점 계산
#         students_total.append(total)
#         # 74.6, 92.55000000000001, 88.8, 99.45, 72.35, 85.85000000000001, 96.25, 68.95, 85.5, 85.75

#     k_score = students_total[K-1] # 인덱스 0부터 시작하기 때문에 k-1로 설정
#     # 99.45, 96.25, 92.55000000000001, 88.8, 85.85000000000001, 85.75, 85.5, 74.6, 72.35, 68.95
#     rank = sorted(students_total)[::-1] # 내림차순으로 정렬

#     rank_top_10 = rank.index(k_score) // (N//10)  # 2
#     k_rank = grades[rank_top_10] # A-

#     print(f'#{tc} {k_rank}')


# 어디에 단어가 들어갈 수 있을까
# n*n 크기의 퍼즐 내에 특정 길이 k를 갖는 단어가 들어갈 수 있는 자리의 수를 구하시오.

# T = int(input())

# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     puzzle = [list(map(int, input().split())) for _ in range(n)]
#     total = 0

#     for i in range(n):
#         cnt = 0
#         # 행 우선 순회
#         for j in range(n):
#             if puzzle[i][j] == 1: # 빈칸일 때
#                 cnt += 1 # cnt 변수에 1를 더함
#             if puzzle[i][j] == 0 or j == n-1: # 빈칸이 아니거나 끝에 닿았을 때
#                 if cnt == k: # cnt 변수에 저장된 값이 k와 같다면
#                     total += 1 # total 변수에 1를 더한다
#                 cnt = 0 # cnt 변수는 초기화
#         # 열 우선 순회
#         for j in range(n):
#             if puzzle[j][i] == 1:
#                 cnt += 1
#             if puzzle[j][i] == 0 or j == n-1:
#                 if cnt == k:
#                     total += 1
#                 cnt = 0
#     print(f'#{tc} {total}')


# 암호생성기
# 첫번째 숫자를 1감소한 뒤 맨 뒤로 보낸다(이 과정을 5번 == 1싸이클)
# 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료되고 이때의 8자리 숫자가 암호가 된다.

# for tc in range(1, 11):
#     N = int(input())
#     queue = list(map(int, input().split()))
#     flag = 0  # while문 종료조건

#     while True:
#         for i in range(1, 6):  # 1 2 3 4 5
#             n = queue.pop(0)  # n 이라는 변수를 생성(queue 리스트 첫 번째 요소를 제거)
#             if n-i <= 0:  # 숫자가 감소할 때, 0이거나 작다면
#                 queue.append(0)  # 그 값은 유지되며 프로그램은 종료되고 이때의 숫자가 암호가 된다
#                 flag = 1
#                 break
#             queue.append(n-i)  # 그게 아니라면 n번째 숫자를 i만큼 감소하여 맨뒤로 보낸다.

#         if flag:
#             break

#     print(f'#{tc}', *queue)


# 괄호 짝짓기
# 4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.
# 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성.
# 맞으면 1, 틀리면 0

# for tc in range(1, 11):
#     n = int(input())
#     bracket = input()
#     stack = []

#     for i in bracket:
#         if not stack: # 처음에 stack 리스트가 비어있을 경우
#             stack.append(i) # 리스트에 i를 추가
#         else: 
#             if (stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}') or (stack[-1] == '<' and i == '>'):
#                 stack.pop() # 리스트의 마지막이 여는 괄호면서 i가 닫는 괄호라면 리스트에서 삭제
#             else:
#                 stack.append(i) # 아니라면 리스트에 i 추가

#     answer = 1 if not stack else 0 # 리스트가 빈다면 1, 아니라면 0
#     print(f'#{tc} {answer}')