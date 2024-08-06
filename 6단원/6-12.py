# 비재귀적인 퀵 정렬 구현하기

from typing import MutableSequence
from stack import Stack

def qsort(a:MutableSequence, left:int, right:int) -> None:
    range = Stack(right - left + 1)

    range.push((left,right))

    while not range.is_empty():
        pl,pr = left, right = range.pop()
        x = a[(left + right)//2]

    while pl <= pr:
        while a[pl] < x:pl += 1
        while a[pr] > x:pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pr += 1
            pl -+ 1

    if left < pr: range.push((left,pr))
    if pl < right: range.push((pl,right))

num = int(input('원소 수를 입력하세요.:'))
x=[None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]={x[i]}:'))

qsort(x)

print(x)

