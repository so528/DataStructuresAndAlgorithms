# 왼쪽 아래가 직각인 이등변 삼각형으로 *출력하기

n=int(input('짧은 변의 길이를 입력하세요.:'))

for x in range (1,n+1,1):
    for y in range (1,x+1,1):
        print('*', end='')
    print()
