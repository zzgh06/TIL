# 파일 정리
# 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
# 보기 편하게 확장자들을 사전 순으로 정렬해 줘
# 알고리즘 분류 : 자료 구조, 문자열 정렬, 해시를 사용한 집합과 맵, 파싱
import sys
input = sys.stdin.readline

n = int(input())

files = dict()

for _ in range(n):
    extends = input().rstrip().split('.')
    # print(extends) sbrus.txt ['sbrus', 'txt'] / spc.spc ['spc', 'spc']
    if extends[1] not in files:
        files[extends[1]] = 1
    else:
        files[extends[1]] += 1
# print(files) {'txt': 1, 'spc': 1}

files = sorted(files.items())
# print(files) [('icpc', 2), ('spc', 2), ('txt', 3), ('world', 1)]

for key, value in files:
    print(key, value)
