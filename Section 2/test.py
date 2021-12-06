
import sys
sys.stdin=open("/Users/jeongin/Desktop/Algorithm/python_algorithm/Section 2/input.txt", "rt")
n, k = list(map(int, input().split())) #띄어쓰기로 구분해서 int로 읽어옴
cnt = 0
for i in range(1, n+1):
   if n%1 == 0:
       cnt += 1
   if cnt == k:
       print(i)
       break
else: #for문이 정상적으로 끝나지 않으면
   print(-1)