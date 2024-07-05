# 리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    lst[idx] = val

x = [1,2,3,4,5,]
print('x=', x)

index = int(input('업데이트 할 인덱스를 선택하세요.:'))
value = int(input('새로운 값을 입력하세요.:'))

change(x,index,value)
print(f'x={x}')
