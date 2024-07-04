# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

while True:
    n=int(input('몇 까지 더할까요?:'))
    if n > 0:
        break

sum=0
x=1

for x in range (1,n+1,1):
    sum += x

print(sum)
