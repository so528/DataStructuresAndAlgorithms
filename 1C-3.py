# 2자리 양수 (10~99) 입력받기


while True:
    n = int(input('두 자리 양수를 입력하세요: '))
    if 10 <= n <= 99:
        break

print(f'양수는 {n}입니다.')

