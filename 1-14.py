# *를 n개를 출력하되 w개마다 줄바꿈하기1

n=int(input('*를 몇 개 출력할까요?:'))
w=int(input('몇 개 마다 줄바꿈 할까요?:'))

for x in range(n):
    print('*',end="")
    if x % w == w-1:
        print()

if n % w:
    print()
