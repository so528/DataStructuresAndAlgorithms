# 이진 삽입 정렬 알고리즘 구현(bisect.insort 사용)

from typing import MutableSequence
import bisect

def binary_insertion_sort(a:MutableSequence) -> None:
    for i in range(1,len(a)):
        bisect.insort(a,a.pop(i),0,i)


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)
    print('정렬된 배열:')
    print(x)