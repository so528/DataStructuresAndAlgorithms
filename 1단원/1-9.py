# a부터 b까지 정수의 합 구하기(for문)

a=int(input('a를 입력하세요.:'))
b=int(input('b를 입력하세요.:'))

sum = 0

if a > b:
    a,b = b,a

for x in range (a,b+1,1):
    sum += x
    
    
    
print(sum)
