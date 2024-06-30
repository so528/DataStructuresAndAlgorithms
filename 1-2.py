#세 정수의 최댓값 구하기

def maximum(a,b,c):
    maximum=a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    return maximum

print(maximum(1,2,3))
print(maximum(1,3,2))
print(maximum(2,1,3))
print(maximum(2,3,1))
print(maximum(3,1,2))
print(maximum(3,2,1))

