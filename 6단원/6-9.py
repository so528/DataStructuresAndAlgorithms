# 셸 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)

from typing import MutableSequence

def shell_sort(a:MutableSequence) -> None:

    n = len(a)
    h = 1

    while h < n // 9:
        h = h*3 + 1

    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3



if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))
    
    shell_sort(x)
    print('정렬된 배열:')
    print(x)