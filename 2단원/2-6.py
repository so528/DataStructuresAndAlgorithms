# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> Any:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('원소를 역순으로 배열합니다.')
    k = int(input('원소의 개수를 입력하세요.:'))
    x = [None] * k

    for i in range(k):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(k):
        print(f'x[{i}]={x[i]}')

