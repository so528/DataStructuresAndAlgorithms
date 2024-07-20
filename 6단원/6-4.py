
# 버블 정렬 알고리즘 구현하기(알고리즘의 개선2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last

if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]를 입력하세요: '))

    bubble_sort(x)
    
    for i in range(n):
        print(f'x[{i}] = {x[i]}')

