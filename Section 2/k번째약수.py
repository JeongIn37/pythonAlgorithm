f = open("/Users/jeongin/Desktop/Algorithm/python_algorithm/Section 2/input.txt", "rt") 
line = f.readlines()

#자연수 p,q에 대해 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수
#두 자연수 N, K가 주어졌을 때 N의 약수들 중에서 K번째로 작은 수를 출력하는 프로그램을 작성하시오
#약수가 K개보다 적어서 K번째가 존재하지 않을 경우 -1 출력

N, K = map(int, input().split())
