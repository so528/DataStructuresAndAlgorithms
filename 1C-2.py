# 세 정수를 입력받아 중앙값 구하기

a=int(input('a를 입력하세요.'))
b=int(input('b를 입력하세요.'))
c=int(input('c를 입력하세요.'))

def med3(a,b,c):
    if a >= b:
        if b > c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c :    # b > a
        return a
    elif b > c :
        return c
    else:
        return b

print('중앙값은', med3(a,b,c), '입니다.')
            
      
