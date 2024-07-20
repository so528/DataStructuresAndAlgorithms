from typing import MutableSequence

def bubble_sort_verbose(a: MutableSequence) -> None:
    """버블 정렬(정렬 과정을 출력)"""
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수

    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + (' ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                                    end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]

        for m in range(0, n - 1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]를 입력하세요: '))

    bubble_sort_verbose(x)
    
    for i in range(n):
        print(f'x[{i}] = {x[i]}')


