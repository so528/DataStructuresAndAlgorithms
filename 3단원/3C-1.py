# seq_search() 함수를 이용하여 실수 검색하기


from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    else:
        return -1

print('실수를 검색합니다.')
print('End를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]를 입력하세요.:')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

k = float(input('검색할 값을 입력하세요.:'))

idx = seq_search(x,k)

if idx == -1:
    print('검색에 실패했습니다.')
else:
    print(f'검색한 값은 x[{idx}]입니다.')
