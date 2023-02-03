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