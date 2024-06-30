# 세 정수를 입력받아 중앙값 구하기 2

a=int(input('a를 입력하세요.:'))
b=int(input('b를 입력하세요.:'))
c=int(input('c를 입력하세요.:'))


def med3(a,b,c):
    if (b >= a and c <= a) or (c >= a and b <= a):
        return a
    elif (a >= b and b >= c) or (c >= b and b >= a):
        return b
    else:
        return c

print('중앙값은', med3(a,b,c), '입니다.')
