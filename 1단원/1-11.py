# a부터 b까지 정수의 합 구하기2

a=int(input('a를 입력하세요.:'))
b=int(input('b를 입력하세요.:'))

sum=0

if a > b:
    a,b=b,a

for x in range (a,b,1):
    sum += x
    print(x,'+', end="")

sum += b
print(b,'=',sum ,end="")

    
