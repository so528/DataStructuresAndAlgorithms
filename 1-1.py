#세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')

a=int(input('a를 입력하세요.'))
b=int(input('b를 입력하세요.'))
c=int(input('c를 입력하세요.'))

maximum=a

if b > a:
    maximum = b

if c > a:
    maximum = c

print('최댓값은', maximum, '입니다.')
