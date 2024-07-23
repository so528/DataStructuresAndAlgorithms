# 단순 선택 정렬 알고리즘 구현하기

from typing import MutableSequence

def selection_sort(a:MutableSequence) -> None:
    n=len(a)
    for i in range(n-1):
        min = i
        for j in range(i + 1,n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


n = int(input('원소의 개수를 입력하세요.:'))
x = [None] * n

for i in range(n):
    x[i] = int(input(f'x[{i}]:'))

selection_sort(x)

print(x)

