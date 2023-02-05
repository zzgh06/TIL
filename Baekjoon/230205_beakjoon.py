# 2839 : 설탕 배달

n = int(input())
cnt = 0

while n >= 0: # 설탕이 있으면
  if n % 5 == 0: # n의 값이 5의 배수이고, 0일때
    cnt += int(n // 5) # 5로 나눈 몫을 더해줌
    print(cnt)
    break
  
  n -= 3 # 5의 배수가 아닐 경우 n의 값에서 3를 빼준다(3kg 봉지)
  cnt += 1
  
else:
  print(-1) # 5와 3으로 나눌 수 없는 정수일 경우 -1를 출력한다