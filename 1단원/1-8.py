# 1부터 n까지 정수의 합 구하기2(for문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('정수를 입력하세요.:'))
sum=0
x=1

for x in range(1,n+1,1):
    sum += x

print(sum)
