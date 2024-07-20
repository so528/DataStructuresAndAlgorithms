from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break

if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]를 입력하세요: '))

    bubble_sort(x)
    
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
