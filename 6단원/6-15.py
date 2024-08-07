# 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int, buff: MutableSequence) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center, buff)
            _merge_sort(a, center + 1, right, buff)

            p = j = 0  
            i = k = left 

            while i <= center: # p는 버퍼의 right,j는 left,i는 a의 center,k는left
                buff[p] = a[i] 
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1, buff)
    del buff

if __name__ == '__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
