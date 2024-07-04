# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

n=int(input('짧은 변의 길이를 입력하세요.:'))

for x in range (n):
    for _ in range (n-x-1):
        print(' ', end="")
    for _ in range (x+1):
        print('*',end='')
    print()
