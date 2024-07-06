# while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key:Any) -> int:
    i=0
    while True:
        if i == len(a):
            return -1

        if a[i] == key:
            return i

        i+=1
            
if __name__=='__main__':
    num = int(input('원소 수를 입력하세요.:'))
    x = [None] * num
    for y in range(num):
        x[y] = int(input(f'x{[y]} 원소를 입력하세요.:'))
    z = int(input('검색할 값을 입력하세요.:'))

    idx = seq_search(x,z)

    if idx == -1:
        print('검색에 실패했습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
    
