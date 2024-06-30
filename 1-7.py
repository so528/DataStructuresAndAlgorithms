# 1부터 n까지 정수의 합 구하기 1(while문)

print('1부터 n까지 정수의 합을 구합니다.')
n=int(input('정수를 입력하세요.:'))

sum=0
x=1

while x <= n:
    sum += x
    x += 1

print(sum)
    
