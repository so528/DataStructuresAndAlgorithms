# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기

def cord_conv(x: int, r:int):
    d=''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]
