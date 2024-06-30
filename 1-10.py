a = int(input('a를 입력하세요.: '))
b = int(input('b를 입력하세요.: '))

sum = 0

for x in range(a, b + 1):
    sum += x

    if x < b:
        print(f"{x} + ", end="")
    else:
        print(f"{x} = ", end="")
print(sum)

