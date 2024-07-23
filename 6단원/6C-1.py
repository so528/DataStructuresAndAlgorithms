# 이진 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        
        while pl <= pr:
            pc = (pl + pr) // 2
            if a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

        pd = pl
        
        
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        
        a[pd] = key

if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)
    print('정렬된 배열:')
    print(x)
