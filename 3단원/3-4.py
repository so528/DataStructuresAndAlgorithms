# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a:Sequence, key:Any) -> int:
    pl = 0
    pr = len(a)-1
    pc = (pl + pr) // 2

    while True:
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pr = pc -1
        else:
            pl = pc +1

        if pl > pc:
            break
        return -1

if __name__=='__main__':
    num = int(input('원소의 수를 입력하세요.:'))
    x = [None] * num
    print('원소를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]:'))

    for i in range (1,num,1):   
        while True:
            x[i] = int(input(f'x[{i}]:'))
            if x[i-1] < x[i]:
                break
    k = int(input('검색할 값을 입력하세요.:'))

    idx = bin_search(x,k)
    if idx == -1:
        print('검색에 실패했습니다.')
    else:
        print(f'검색한 값은 x[{idx}]입니다.')
            

    
            
            
        
