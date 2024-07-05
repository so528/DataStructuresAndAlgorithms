def card_conv(no: int, cd: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while no > 0:
        d += dchar[no % cd]
        no //= cd
    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        no = int(input('변환할 음수가 아닌 정수를 입력하세요.: '))
        if no >= 0:
            break

    while True:
        cd = int(input('몇 진수로 변환할까요?: '))
        if 2 <= cd <= 36:  
            break

    print(f'{no}을 {cd}진수로 변환합니다.')
    print(f'결과는 {card_conv(no, cd)}입니다.')


    
