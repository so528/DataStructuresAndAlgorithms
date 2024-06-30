# *를 n개 출력하되 w개마다 줄바꿈하기 2

n=int(input('*를 몇 개 출력할까요?:'))
w=int(input('몇 개마다 줄바꿈할까요?:'))

for _ in range(n//w):
    print('*'*w)


rest= n % w

if rest:
    print('*'*(n % w))


