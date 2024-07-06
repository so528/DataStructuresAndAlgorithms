# 선형 검색 알고리즘 (3C-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key:Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    if i == len(seq):
        return -1
    else:
        return i

if __name__=='__main__':
    num = int(input('원소의 수를 입력하세요.:'))
    x =[None] * num
    for k in range(num):
        x[k] = int(input(f'x[{k}]값을 입력하세요.:'))
    ky = int(input('검색할 값을 입력하세요.:'))

    idx = seq_search(x,ky)

    if idx == -1:
        print('검색값이 없습니다.')
    else:
        print(f'검색값은 x[{idx}]입니다.')

    
 
