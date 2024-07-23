# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp :
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__=='__main__':
    n = int(input('원소의 개수를 입력하세요.:'))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    
    insertion_sort(x)

    print(x)