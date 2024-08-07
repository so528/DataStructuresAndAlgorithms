# 퀵 정렬 알고리즘 구현하기(원소 수가 9 미만이면 단순 삽입 정렬) 

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]를 오름차순으로 정렬하고 중앙값의 인덱스를 반환"""
    if a[idx2] < a[idx1]:
        a[idx1], a[idx2] = a[idx2], a[idx1]
    if a[idx3] < a[idx2]:
        a[idx2], a[idx3] = a[idx3], a[idx2]
    if a[idx2] < a[idx1]:
        a[idx1], a[idx2] = a[idx2], a[idx1]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > left and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        x = a[(left + right) // 2]

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)  # 여기에서 함수 이름을 quick_sort에서 qsort로 변경해야 합니다.
        if pl < right: qsort(a, pl, right)  # 여기에서 함수 이름을 quick_sort에서 qsort로 변경해야 합니다.

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')



