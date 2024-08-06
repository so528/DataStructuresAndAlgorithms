# 배열 두 그룹으로 나누기

from typing import MutableSequence

def partition(a:MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] < x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

num = int(input('원소 수를 입력하세요.:'))
x=[None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]={x[i]}:'))

partition(x)

print(x)